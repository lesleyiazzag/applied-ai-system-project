# 🎧 Model Card: Music Recommender Simulation + Reliability System

## 1. Model Name

VibeMatch 1.0 (Extended with Reliability Testing)

---

## 2. Intended Use

This system is designed to recommend songs based on a user’s preferences for genre, mood, and musical features such as energy and danceability.

It is intended for educational use only and demonstrates how simple recommendation systems work using rule-based scoring rather than machine learning models.

The system assumes users have stable preferences that can be represented as structured numerical and categorical inputs.

---

## 3. How the Model Works

The recommender assigns a score to each song based on how well it matches a user’s preferences.

It uses:
- Genre and mood matching (categorical signals)
- Numerical similarity for features like energy, valence, and danceability
- Weighted scoring to combine these signals into a final ranking

Songs are sorted by total score, and the highest-ranked items are returned as recommendations.

A consistency testing system checks whether repeated runs with the same input produce identical rankings.

---

## 4. Data

The dataset contains 18 songs stored in a CSV file.

Each song includes:
- genre
- mood
- energy
- valence
- danceability
- tempo
- acousticness

The dataset is small and stylistically limited, which restricts diversity in recommendations.

---

## 5. Reliability and Testing Behavior

A reliability testing system was added to evaluate whether the recommender produces consistent outputs.

It works by:
- Running the recommendation function on fixed inputs
- Checking whether rankings remain identical across runs
- Logging results of each evaluation

During development, a small randomness factor was temporarily introduced to test whether the system could detect inconsistencies. The tester successfully identified unstable behavior, confirming that the evaluation system works as intended.

After removing randomness, the system returned to fully deterministic behavior.

---

## 6. Limitations and Biases

This system has several limitations:

- It relies on a small dataset, which limits recommendation diversity
- It is heavily influenced by manually chosen feature weights
- Energy tends to dominate scoring, sometimes overriding mood or genre
- It does not learn from user feedback or adapt over time

As a result, recommendations can become repetitive or overly narrow.

---

## 7. Safety, Misuse, and Ethical Considerations

Although this system is low-risk, real-world recommender systems built this way could unintentionally reinforce preference loops.

This means users might only see similar types of content repeatedly, reducing exposure to diverse recommendations.

To prevent this in production systems, techniques such as:
- diversity constraints
- fairness adjustments
- feedback-based learning

would be necessary.

---

## 8. AI Collaboration Reflection

AI tools such as Copilot Chat were used to assist in designing scoring logic and structuring feature comparisons.

One helpful suggestion was using normalized distance scoring (e.g., 1 - |difference|) for numerical features like energy and valence, which improved how similarity was calculated.

However, one incorrect suggestion from AI was simplifying all feature weights equally, which reduced recommendation quality by over-prioritizing categorical features and ignoring meaningful numerical differences. This had to be manually corrected.

This highlights the importance of validating AI-generated code rather than accepting it directly.

---

## 9. Overall Reflection

This project demonstrated that recommendation systems are not only about generating outputs, but also about ensuring those outputs are stable, interpretable, and meaningful.

I learned that:
- Small changes in weighting can significantly affect recommendations
- Reliability testing is essential even for simple rule-based systems
- Deterministic output does not guarantee good or diverse recommendations

If extended, I would incorporate feedback loops or embedding-based similarity methods to improve personalization and reduce manual bias in scoring.