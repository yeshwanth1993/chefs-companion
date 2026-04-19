variable "project_id" {
  type        = string
  description = "The GCP project ID"
  default     = "sdlc-og-test"
}

variable "region" {
  type        = string
  description = "The GCP region"
  default     = "us-central1"
}

variable "repository_id" {
  type        = string
  description = "The Artifact Registry repository ID"
  default     = "chefs-companion-pipeline-repo"
}

variable "image_name" {
  type        = string
  description = "The name of the container image"
  default     = "chefs-companion"
}

variable "pipeline_name" {
  type        = string
  description = "The name of the Cloud Deploy pipeline"
  default     = "chefs-companion-pipeline"
}

variable "github_repo_owner" {
  type        = string
  description = "The owner of the GitHub repository"
  default     = "yeshwanth1993"
}

variable "github_repo_name" {
  type        = string
  description = "The name of the GitHub repository"
  default     = "chefs-companion"
}
