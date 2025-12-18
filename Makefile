.PHONY: help install dev-install clean test coverage lint format type-check run

help:
	@echo "Available commands:"
	@echo "  make install        Install the package"
	@echo "  make dev-install    Install with development dependencies"
	@echo "  make run            Run the calculator in interactive mode"
	@echo "  make test           Run unit tests"
	@echo "  make coverage       Run tests with coverage report"
	@echo "  make lint           Run linting checks (flake8)"
	@echo "  make format         Format code with black"
	@echo "  make type-check     Run type checking with mypy"
	@echo "  make clean          Remove build artifacts and cache"
	@echo "  make all            Run lint, type-check, test, and coverage"

install:
	pip install -e .

dev-install:
	pip install -e ".[dev]"
	pip install -r requirements.txt

run:
	python main.py

test:
	pytest tests/

coverage:
	pytest --cov=src --cov-report=html --cov-report=term tests/
	@echo "Coverage report generated in htmlcov/index.html"

lint:
	flake8 src/ tests/

format:
	black src/ tests/ main.py

type-check:
	mypy src/ --ignore-missing-imports

clean:
	rm -rf build/ dist/ *.egg-info
	rm -rf .pytest_cache/ .mypy_cache/ .coverage htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

all: lint type-check test coverage
