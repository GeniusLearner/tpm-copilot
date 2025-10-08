"""
TPM Co-Pilot - Core Agent Logic
Automated document generation for Technical Program Managers
"""

import anthropic
import os
from dotenv import load_dotenv
from typing import Optional

load_dotenv()


class DocumentGenerator:
    """Core document generation engine for TPM workflows"""

    def __init__(self):
        """Initialize the document generator"""
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY not found. Please set it in .env file. "
                "Get your key from: https://console.anthropic.com/"
            )
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-3-5-sonnet-20241022"

    def _generate(self, prompt: str, max_tokens: int = 1024) -> str:
        """Generate content from prompt"""
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                messages=[{"role": "user", "content": prompt}]
            )
            return message.content[0].text
        except Exception as e:
            return f"Error generating content: {str(e)}\n\nPlease check your API configuration and internet connection."

    def generate_agenda(self, meeting_context: str) -> str:
        """
        Generate a structured meeting agenda

        Args:
            meeting_context: Description of the meeting, attendees, and objectives

        Returns:
            Formatted meeting agenda
        """
        prompt = f"""You are an experienced Technical Program Manager assistant. Generate a clear, actionable meeting agenda that follows TPM best practices.

Context: {meeting_context}

Create a well-structured agenda with:

1. **Meeting Objective** - Clear, measurable goal for the meeting
2. **Attendees & Roles** - Who should attend and why
3. **Agenda Items** - 3-5 specific discussion points with:
   - Topic
   - Time allocation
   - Discussion lead
   - Expected outcome
4. **Pre-Work** - What attendees should prepare beforehand
5. **Success Criteria** - How we'll know the meeting was successful

Format the output in clear markdown with appropriate headings and bullet points. Be specific and actionable. Keep it concise but comprehensive."""

        return self._generate(prompt, max_tokens=1500)

    def summarize_thread(self, thread_text: str) -> str:
        """
        Summarize a discussion thread with key takeaways

        Args:
            thread_text: The conversation thread to summarize

        Returns:
            Concise summary with decisions and action items
        """
        prompt = f"""You are an experienced Technical Program Manager assistant. Summarize this discussion thread in a way that's useful for TPMs who need to track decisions and next steps.

Thread:
{thread_text}

Provide a structured summary with:

1. **TLDR** - 2-3 sentence summary of the entire discussion
2. **Key Decisions Made** - Concrete decisions that were agreed upon
3. **Action Items** - Format as:
   - [ ] Action item description (Owner: Name, Due: Date)
4. **Open Questions / Blockers** - Unresolved issues that need follow-up
5. **Context for Future Reference** - Important background that may be needed later

Be concise, actionable, and focus on information a TPM needs to drive the project forward. Use markdown formatting."""

        return self._generate(prompt, max_tokens=1500)

    def generate_status_report(self, updates: str, project_name: Optional[str] = None) -> str:
        """
        Create an executive-ready status report

        Args:
            updates: Weekly updates, progress, issues
            project_name: Optional project name for the report

        Returns:
            Formatted executive status report
        """
        project_header = f"Project: {project_name}\n" if project_name else ""

        prompt = f"""You are an experienced Technical Program Manager assistant. Create an executive-ready status report that clearly communicates project health and progress.

{project_header}
Updates:
{updates}

Format the report as follows:

# Status Report - [Infer project name or use generic]

**Status: [Green/Yellow/Red]** - Based on the updates

## Executive Summary
2-3 sentences on overall project health and key highlights. Should be readable by execs in 30 seconds.

## Progress This Week
- ✅ Key accomplishments (3-5 bullet points)
- Focus on outcomes, not activities

## Upcoming Milestones
- 📅 Next 1-2 weeks (specific, date-driven)

## Risks & Blockers
- 🚨 **[Severity]** Issue description
  - Impact: What happens if not resolved
  - Mitigation: Proposed solution
  - Owner: Who's handling it

## Metrics / KPIs
[If any metrics are mentioned, present them clearly]

## Support Needed
[Decisions needed from leadership or cross-functional support required]

Use clear, executive-friendly language. Be honest about risks. Focus on what matters."""

        return self._generate(prompt, max_tokens=2000)

    def analyze_risks(self, project_description: str) -> str:
        """
        Identify and analyze potential project risks

        Args:
            project_description: Description of the project, scope, timeline, team

        Returns:
            Comprehensive risk analysis with mitigation strategies
        """
        prompt = f"""You are an experienced Technical Program Manager assistant specializing in risk management. Analyze this project for potential risks across multiple dimensions.

Project Description:
{project_description}

Provide a comprehensive risk analysis:

# Risk Analysis

## Technical Risks
For each risk:
- **Risk**: Clear description
- **Probability**: High/Medium/Low
- **Impact**: High/Medium/Low
- **Mitigation**: Specific, actionable strategy
- **Owner**: Suggested role (e.g., Tech Lead, TPM)
- **Timeline**: When to implement mitigation

Cover 3-5 technical risks (architecture, scalability, tech debt, dependencies, etc.)

## Schedule Risks
Identify 2-3 timeline-related risks (delays, estimation accuracy, dependencies)

## Resource Risks
Identify 2-3 people/team-related risks (capacity, skills, attrition, cross-team dependencies)

## Dependency Risks
Identify external dependencies that could impact the project

## Risk Summary Matrix
Present top 5 risks in priority order (based on Probability × Impact)

Be specific, actionable, and realistic. Focus on risks that TPMs can actually manage or escalate."""

        return self._generate(prompt, max_tokens=2500)

    def create_project_charter(self, project_info: str) -> str:
        """
        Create a project charter from high-level information

        Args:
            project_info: Basic project information

        Returns:
            Formatted project charter
        """
        prompt = f"""You are an experienced Technical Program Manager assistant. Create a project charter that clearly defines project scope, objectives, and stakeholders.

Project Information:
{project_info}

Create a comprehensive project charter:

# Project Charter: [Infer project name]

## Executive Sponsor
[Suggest based on context or TBD]

## Project Overview
Clear description of what we're building and why it matters

## Business Objectives
- Specific, measurable business goals this project achieves
- Tie to company OKRs or strategic initiatives where possible

## Success Criteria
Concrete, measurable criteria (e.g., "Reduce load time by 50%", "Support 1M users")

## Scope

### In Scope
- What we ARE building

### Out of Scope
- What we are NOT building (to prevent scope creep)

## Key Stakeholders
- **Sponsor**: Who's accountable
- **TPM**: Program manager
- **Engineering Lead**: Technical ownership
- **Product**: Requirements and prioritization
- **Design**: UX ownership
- **Other**: QA, Security, etc.

## High-Level Timeline
Major phases and milestones (month-level)

## Key Risks
Top 3 risks at project inception

## Dependencies
Critical dependencies on other teams/projects

## Success Metrics
How we'll measure if the project succeeded (30/60/90 day metrics)

Be specific and realistic. This charter should be a north star for the project team."""

        return self._generate(prompt, max_tokens=2500)
