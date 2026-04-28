# 🎵 Music Recommender Simulation + Reliability Testing System

Loom Video Walkthrough Link - https://www.loom.com/share/10aeeb46485649b081d685bef706d88a

---

## 1. Original Project (Modules 1–3)

The original project was a Music Recommender Simulation that demonstrates how recommendation systems can rank items using structured data. It used a rule-based scoring system to match songs to a user’s preferences based on features like genre, mood, and energy.

The goal was to model simplified versions of real-world systems like Spotify or YouTube, where content is ranked based on feature similarity and weighted scoring rather than deep learning models.

---

## 2. Project Summary

This extended version builds a **Reliability and Consistency Testing System** on top of the original recommender.

The system:
- Generates ranked music recommendations
- Tests whether outputs are consistent across repeated runs
- Logs system behavior for debugging and validation

This makes the system closer to real AI pipelines, where correctness alone is not enough — reliability and repeatability are also required.

---

## 3. Architecture Overview

The system follows this pipeline:

User Input → Load Songs (CSV) → Scoring Function → Ranking Function → Consistency Tester → Logging → Output to User

### System Diagram
See: `/assets/system_architecture.png`

### Key Components:
- **Loader**: Reads song data from CSV
- **Scoring Function**: Computes preference match score
- **Ranking Function**: Sorts songs by score
- **Consistency Tester**: Verifies deterministic outputs
- **Logger**: Tracks system execution and validation steps

---

## 4. Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/lesleyiazzag/applied-ai-system-project.git
cd applied-ai-system-project

### 2. Run the program
```bash
python -m src.main

### 3. Run reliability tests
python -m pytest

---
## Sample Interactions
Example 1: High Energy Pop User

user_prefs = {
    "genre": "pop",
    "mood": "happy",
    "energy": 0.9
}

Output:
Song A — Score: 8.7 (genre + mood + energy match)
Song B — Score: 8.1 (partial energy match)

Example 2: Chill Listener

user_prefs = {
    "genre": "lofi",
    "mood": "calm",
    "energy": 0.2
}

Output:
Chill Beats — Score: 9.2
Soft Waves — Score: 8.8

---
### Design Decisions
A weighted scoring system was used because it is interpretable and closely mirrors early-stage recommendation systems.

Genre and mood were weighted more heavily than numerical features because they represent stronger categorical signals.

Trade-offs:
Simplicity vs realism (no ML models used)
Interpretability vs personalization depth

---
### Testing Approach
This project includes a built-in reliability testing system that checks whether the recommender produces consistent outputs for the same user preferences.

A consistency test is automatically run for each user profile. The system:
- Runs the recommendation function twice on the same input
- Compares ranked outputs and scores
- Flags any differences in ordering or scoring

In addition, a logging system records when tests are executed.

To validate the reliability system, a temporary randomness factor was introduced into the scoring function. This caused inconsistency detection to trigger, confirming that the tester successfully identifies unstable outputs. After removing the randomness, the system returned to fully deterministic behavior.

### Results Summary
- 4 user profiles were tested: High-Energy Pop, Chill Lofi, Intense Rock, and Conflicting Vibe
- The consistency test passed for all runs (no mismatches detected)
- The recommender produced stable rankings across repeated executions
- Log output confirmed test execution for each profile:
  - `[LOG] Testing consistency for 18 songs...`
  - `✅ Consistency check passed.`

    ### Observations
    - The system is deterministic: identical inputs always produce identical rankings
    - Energy similarity heavily influences ranking stability
    - Genre and mood matching help differentiate top results, but energy remains the dominant factor

    ### What Worked Well
    - Ranking order remained stable across repeated runs
    - No inconsistencies were detected in scoring or sorting
    - Logging successfully tracked evaluation steps

    ### Issues Observed
    - Some songs repeatedly appear across multiple profiles due to strong energy similarity
    - The system is sensitive to dataset size, which limits diversity in outputs

---
### Reflection

This project helped me understand how recommendation systems translate structured data into ranked predictions. Even simple recommendation systems require reliability testing to ensure consistent behavior. This implementation demonstrates that deterministic scoring and sorting can produce stable outputs, but also highlights how dataset limitations and feature weighting affect perceived recommendation quality.