# Artifact Registry Repository
resource "google_artifact_registry_repository" "main" {
  location      = var.region
  repository_id = var.repository_id
  description   = "Docker repository for Chef's Companion Pipeline"
  format        = "DOCKER"
}

# Service Accounts
resource "google_service_account" "cloud_build_sa" {
  account_id   = "chefs-companion-cb-sa"
  display_name = "Cloud Build Service Account for Chefs Companion"
}

resource "google_service_account" "cloud_deploy_sa" {
  account_id   = "chefs-companion-cd-sa"
  display_name = "Cloud Deploy execution Service Account for Chefs Companion"
}

resource "google_service_account" "cloud_run_sa" {
  account_id   = "chefs-companion-run-sa"
  display_name = "Cloud Run runtime Service Account for Chefs Companion"
}

# IAM Roles for Cloud Build
resource "google_project_iam_member" "cb_log_writer" {
  project = var.project_id
  role    = "roles/logging.logWriter"
  member  = "serviceAccount:${google_service_account.cloud_build_sa.email}"
}

resource "google_project_iam_member" "cb_ar_writer" {
  project = var.project_id
  role    = "roles/artifactregistry.writer"
  member  = "serviceAccount:${google_service_account.cloud_build_sa.email}"
}

resource "google_project_iam_member" "cb_deploy_releaser" {
  project = var.project_id
  role    = "roles/clouddeploy.releaser"
  member  = "serviceAccount:${google_service_account.cloud_build_sa.email}"
}

resource "google_project_iam_member" "cb_service_account_user" {
  project = var.project_id
  role    = "roles/iam.serviceAccountUser"
  member  = "serviceAccount:${google_service_account.cloud_build_sa.email}"
}

# IAM Roles for Cloud Deploy
resource "google_project_iam_member" "cd_run_admin" {
  project = var.project_id
  role    = "roles/run.admin"
  member  = "serviceAccount:${google_service_account.cloud_deploy_sa.email}"
}

resource "google_project_iam_member" "cd_service_account_user" {
  project = var.project_id
  role    = "roles/iam.serviceAccountUser"
  member  = "serviceAccount:${google_service_account.cloud_deploy_sa.email}"
}

resource "google_project_iam_member" "cd_log_writer" {
  project = var.project_id
  role    = "roles/logging.logWriter"
  member  = "serviceAccount:${google_service_account.cloud_deploy_sa.email}"
}

resource "google_project_iam_member" "cd_releaser" {
  project = var.project_id
  role    = "roles/clouddeploy.releaser"
  member  = "serviceAccount:${google_service_account.cloud_deploy_sa.email}"
}

resource "google_project_iam_member" "cd_job_runner" {
  project = var.project_id
  role    = "roles/clouddeploy.jobRunner"
  member  = "serviceAccount:${google_service_account.cloud_deploy_sa.email}"
}

# Developer Connect Git Repository Link
resource "google_developer_connect_git_repository_link" "main" {
  location      = var.region
  project       = var.project_id
  connection_id = "03a42fe9-b4ef-4aa2-a9c8-238869c674b9"
  git_repository_uri = "https://github.com/${var.github_repo_owner}/${var.github_repo_name}.git"
  repository_link_id = "chefs-companion"
}

# Cloud Build Trigger
resource "google_cloudbuild_trigger" "main" {
  location = var.region
  name     = "chefs-companion-push-main"

  developer_connect_event_config {
    git_repository_link = google_developer_connect_git_repository_link.main.id
    push {
      branch = "^main$"
    }
  }

  service_account = google_service_account.cloud_build_sa.id
  filename        = "cloudbuild.yaml"

  substitutions = {
    _AR_HOSTNAME   = "${var.region}-docker.pkg.dev"
    _AR_REPO_NAME  = google_artifact_registry_repository.main.repository_id
    _IMAGE_NAME    = var.image_name
    _PIPELINE_NAME = var.pipeline_name
    _REGION        = var.region
  }
}

# Cloud Deploy Delivery Pipeline
resource "google_clouddeploy_delivery_pipeline" "main" {
  location = var.region
  name     = var.pipeline_name

  serial_pipeline {
    stages {
      target_id = "staging"
    }
    stages {
      target_id = "prod"
    }
  }
}

# Cloud Deploy Staging Target
resource "google_clouddeploy_target" "staging" {
  location = var.region
  name     = "staging"

  run {
    location = "projects/${var.project_id}/locations/${var.region}"
  }

  execution_configs {
    usages            = ["RENDER", "DEPLOY"]
    service_account   = google_service_account.cloud_deploy_sa.email
  }
}

# Cloud Deploy Production Target
resource "google_clouddeploy_target" "prod" {
  location = var.region
  name     = "prod"

  run {
    location = "projects/${var.project_id}/locations/${var.region}"
  }

  execution_configs {
    usages            = ["RENDER", "DEPLOY"]
    service_account   = google_service_account.cloud_deploy_sa.email
  }

  require_approval = true
}

# Cloud Deploy Automation (Rollback on Failure)
resource "google_clouddeploy_automation" "rollback_on_failure" {
  location          = var.region
  name              = "${var.pipeline_name}-rollback"
  delivery_pipeline = google_clouddeploy_delivery_pipeline.main.name
  service_account   = google_service_account.cloud_deploy_sa.email
  
  selector {
    targets {
      id = "*"
    }
  }

  rules {
    rollback_rule {
      id = "rollback-on-failure"
    }
  }

  suspended = false
}
