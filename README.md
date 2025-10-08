# TPM Co-Pilot

An AI-powered documentation assistant that helps Technical Program Managers automate repetitive documentation tasks.

[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.39-FF4B4B)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Problem Space

Technical Program Managers spend significant time on documentation tasks that follow predictable patterns:

- **Meeting Agendas**: Similar structure, different content each time
- **Thread Summaries**: Extracting decisions from long Slack/email threads
- **Status Reports**: Weekly updates in consistent executive format
- **Risk Documentation**: Identifying and categorizing project risks
- **Project Charters**: Standard templates with project-specific details

These tasks are necessary but repetitive - ideal candidates for AI assistance.

---

## Solution

TPM Co-Pilot takes unstructured input and generates structured documentation:

| Task | Input | Output |
|------|-------|--------|
| Meeting Agenda | Meeting context, objectives | Structured agenda with time allocations |
| Thread Summary | Slack/email thread | TLDR, decisions, action items |
| Status Report | Raw weekly updates | Executive-ready report |
| Risk Analysis | Project description | Categorized risks with mitigations |
| Project Charter | High-level project info | Complete charter document |

---

## Target Users

**Primary: Technical Program Managers**
- Managing multiple projects
- Heavy documentation workload
- Need consistent output quality

**Secondary: Engineering Managers**
- Running team meetings
- Reporting to leadership
- Tracking project risks

**Tertiary: Product Managers**
- Cross-functional coordination
- Stakeholder communication

---

## Features

### 1. Meeting Agenda Generator
- Objectives and success criteria
- Timed discussion points
- Pre-work items
- Attendee roles

### 2. Thread Summarizer
- TLDR summary
- Key decisions made
- Action items with owners
- Open questions

### 3. Status Report Builder
- Project health indicators
- Key accomplishments
- Upcoming milestones
- Risks and blockers

### 4. Risk Analyzer
- Technical risks
- Schedule risks
- Resource risks
- Mitigation strategies

### 5. Project Charter Creator
- Objectives and scope
- Stakeholders
- Timeline and milestones
- Success metrics

---

## Product Decisions

**Why Streamlit over React/Next.js?**
- Faster to build for MVP
- Python ecosystem (familiar to TPMs who script)
- Built-in UI components for forms
- Easy deployment

**Why separate tools vs. one chat interface?**
- Each tool has specific input/output
- Guided workflows reduce errors
- Easier to iterate on individual features

**Why these 5 features?**
- Maps to core TPM documentation needs
- High frequency tasks
- Clear input → output patterns

---

## Tech Stack

| Component | Technology | Rationale |
|-----------|------------|-----------|
| Language | Python 3.9+ | Rapid development, AI libraries |
| UI | Streamlit | Fast prototyping, built-in components |
| AI | Anthropic Claude | Strong at structured document generation |
| Config | python-dotenv | Simple environment management |

---

## Architecture

```
tpm-copilot/
├── app.py              # Streamlit UI and routing
├── config.py           # Environment configuration
├── core/
│   └── agent.py        # AI document generation
├── utils/
│   └── helpers.py      # Utility functions
└── requirements.txt
```

---

## Quick Start

```bash
pip install -r requirements.txt
cp .env.example .env
# Add ANTHROPIC_API_KEY to .env
streamlit run app.py
```

Opens at `http://localhost:8501`

---

## Roadmap

### Phase 1: Current (MVP)
- [x] 5 core documentation tools
- [x] Web-based UI
- [x] Template examples

### Phase 2: Integration
- [ ] Slack integration (direct thread import)
- [ ] Calendar integration (meeting context)
- [ ] Export to Confluence/Notion

### Phase 3: Team Features
- [ ] Shared templates
- [ ] Team-specific formatting
- [ ] Usage analytics

---

## Learnings

1. **Match the workflow**: Each tool mirrors an actual TPM task
2. **Guided > open-ended**: Specific inputs produce better outputs
3. **Templates help**: Example inputs reduce friction
4. **Web UI for accessibility**: Not everyone is comfortable with CLI

---

## License

MIT License

---

## Contact

**Sanchit Khurana**
- GitHub: [github.com/GeniusLearner](https://github.com/GeniusLearner)
- Email: sanchit@sanchitkhurana.com
