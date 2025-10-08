"""
Configuration settings for TPM Co-Pilot
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Application Settings
APP_NAME = "TPM Co-Pilot"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "Productivity Platform for Technical Program Managers"

# API Configuration
API_KEY = os.getenv("ANTHROPIC_API_KEY")
MODEL_NAME = "claude-3-5-sonnet-20241022"
DEFAULT_MAX_TOKENS = 1024

# Generation Settings
GENERATION_TIMEOUT = 30  # seconds
MAX_CONTEXT_LENGTH = 4000  # characters

# UI Configuration
PAGE_ICON = "⚡"
LAYOUT = "wide"

# Feature Flags
ENABLE_ANALYTICS = True
ENABLE_DOWNLOAD = True
ENABLE_TEMPLATES = True

# Generation Limits (for free tier optimization)
MAX_GENERATIONS_PER_SESSION = 50
