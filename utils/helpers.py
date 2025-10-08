"""
Helper functions for TPM Co-Pilot
"""

import re
from typing import Optional


def validate_input(text: str, min_length: int = 10, max_length: int = 5000) -> tuple[bool, Optional[str]]:
    """
    Validate user input

    Args:
        text: Input text to validate
        min_length: Minimum required length
        max_length: Maximum allowed length

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not text or not text.strip():
        return False, "Input cannot be empty"

    text_length = len(text.strip())

    if text_length < min_length:
        return False, f"Input too short. Minimum {min_length} characters required"

    if text_length > max_length:
        return False, f"Input too long. Maximum {max_length} characters allowed"

    return True, None


def format_output(text: str) -> str:
    """
    Format the generated output for better readability

    Args:
        text: Raw output text

    Returns:
        Formatted text
    """
    # Remove excessive newlines
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Ensure proper spacing after headers
    text = re.sub(r'(#{1,6} .+)\n([^\n])', r'\1\n\n\2', text)

    return text.strip()


def calculate_time_saved(task_type: str) -> dict:
    """
    Calculate time savings for different task types

    Args:
        task_type: Type of task (agenda, summary, report, risk, charter)

    Returns:
        Dictionary with manual_time, automated_time, time_saved, percentage
    """
    time_savings = {
        'agenda': {'manual': 45, 'automated': 2, 'unit': 'minutes'},
        'summary': {'manual': 30, 'automated': 1, 'unit': 'minutes'},
        'report': {'manual': 60, 'automated': 3, 'unit': 'minutes'},
        'risk': {'manual': 90, 'automated': 5, 'unit': 'minutes'},
        'charter': {'manual': 180, 'automated': 10, 'unit': 'minutes'}
    }

    if task_type not in time_savings:
        return {}

    data = time_savings[task_type]
    manual_time = data['manual']
    automated_time = data['automated']
    time_saved = manual_time - automated_time
    percentage = int((time_saved / manual_time) * 100)

    return {
        'manual_time': manual_time,
        'automated_time': automated_time,
        'time_saved': time_saved,
        'percentage': percentage,
        'unit': data['unit']
    }


def get_task_name(tool: str) -> str:
    """
    Get standardized task name from tool name

    Args:
        tool: Tool name from UI

    Returns:
        Standardized task name
    """
    mapping = {
        '📋 Meeting Agenda Generator': 'agenda',
        '💬 Thread Summarizer': 'summary',
        '📊 Status Report Builder': 'report',
        '⚠️ Risk Analyzer': 'risk',
        '📄 Project Charter Creator': 'charter'
    }
    return mapping.get(tool, 'unknown')
