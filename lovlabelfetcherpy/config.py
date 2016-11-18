"""config.py example -- configures SPARQL endpoint for data generation."""
import os

PROJECT_ROOT = os.path.join(
    os.path.dirname(
        os.path.realpath(__file__)
    ),
    ".."
)
LOG_FOLDER = os.path.join(PROJECT_ROOT, "logs")
LOG_FILE = os.path.join(LOG_FOLDER, "log.out")
