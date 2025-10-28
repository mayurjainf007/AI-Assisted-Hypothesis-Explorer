#!/usr/bin/env bash
# Usage: ./scripts/gcp_deploy.sh <project-id> <region>
set -euo pipefail
PROJECT=${1:-my-gcp-project}
REGION=${2:-us-central1}
SVC="ai-hypothesis-explorer"

gcloud auth configure-docker us-central1-docker.pkg.dev -q || true
gcloud config set project "$PROJECT"

IMG="us-central1-docker.pkg.dev/$PROJECT/containers/ai-hypothesis-explorer:latest"

# Build & push
docker build -t "$IMG" -f docker/Dockerfile .
gcloud artifacts repositories create containers --repository-format=docker --location="$REGION" --description="Containers" || true
docker push "$IMG"

# Deploy to Cloud Run
gcloud run deploy "$SVC" --image "$IMG" --platform managed --region "$REGION" --allow-unauthenticated --port 8501

echo "Deployed to Cloud Run service: $SVC"
