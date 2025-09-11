# Makefile for CI/CD Analytics Dashboard

# Variables
BACKEND_DIR=backend
FRONTEND_DIR=frontend
VENV=$(BACKEND_DIR)/venv

# Default target
.PHONY: dev
dev: backend-serve frontend-dev

# ---------------------
# Backend Commands
# ---------------------

.PHONY: backend-install
backend-install:
	python3 -m venv $(VENV)
	. $(VENV)/bin/activate && pip install -r $(BACKEND_DIR)/requirements.txt

.PHONY: backend-serve
backend-serve:
	. $(VENV)/bin/activate && uvicorn $(BACKEND_DIR).main:app --reload

# ---------------------
# Frontend Commands
# ---------------------

.PHONY: frontend-install
frontend-install:
	cd $(FRONTEND_DIR) && npm install

.PHONY: frontend-dev
frontend-dev:
	cd $(FRONTEND_DIR) && npm run dev
