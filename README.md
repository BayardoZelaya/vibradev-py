# gym‑chatbot

A lightweight FastAPI-based chatbot for fitness and workout guidance.  
Ask questions, get exercise recommendations, track progress, and more—all via a RESTful API or web UI.

## Features

- Conversational interface for fitness tips and workout plans  
- Support for common workout categories (strength, cardio, flexibility)  
- Easily deployable via Docker and Helm on Kubernetes  
- Automatic image updates with ArgoCD Image Updater  
- CI/CD integration with GitHub Actions and GCP Artifact Registry

## Prerequisites

- Python 3.10+  
- Docker (for container builds)  
- Helm 3 (for Kubernetes deployments)  
- `uv` CLI tool (optional)  
- GCP project with Artifact Registry & GKE cluster  
- GitHub Actions secrets: `GCP_KEY`, `GCP_PROJECT=vibradev-dev`