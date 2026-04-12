# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---
VibeMatch 1.0

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---
This model recommends songs to a user based on their preferences. It tries to find songs with a similar “vibe” using features like genre, mood, and energy.

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---
Each song is given a score based on how well it matches the user’s preferences. The model gives points for matching genre and mood. It also compares numerical features like energy and gives higher scores to songs that are closer to the user’s target value. Songs are then ranked from highest to lowest score, and the top results are recommended.

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---
The dataset contains 18 songs with features including genre, mood, energy, tempo, valence, danceability, and acoustics. The dataset is small and not very diverse, which limits the variety of recommendations.

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---
This system works well when user preferences are clear and consistent. For example, it performs well for profiles like "Chill Lofi" and "Intense Rock," where genre, mood, and energy all align. In these cases, the model correctly ranks songs that match both the emotional tone and intensity of the user’s input.

The scoring system is especially good at capturing energy-based similarity, which helps it distinguish between calm and high-intensity music. It also reliably prioritizes songs that match multiple features at once, which leads to reasonable top recommendations in most cases.

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---
One key limitation of this system is that it over-prioritizes energy, especially after increasing its weight in the scoring formula. This is evident in the results, where songs like "Gym Hero" and "Neon Nights" appear across multiple profiles, even when they do not match the user’s preferred genre or mood.

For example, in the "Conflicting Vibe" profile (high energy but sad mood), the system recommends mostly high-energy songs and completely ignores the mood preference. This shows that the model struggles to balance conflicting features and defaults to the strongest numerical signal.

Additionally, because the dataset is relatively small, the system repeatedly recommends the same songs across different profiles. This creates a limited recommendation space and reduces diversity.

Overall, the system is biased toward numerical similarity (especially energy), which can lead to less accurate recommendations when emotional or categorical features like mood and genre are more important.

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---
I tested the recommender system using multiple user profiles, including "High-Energy Pop," "Chill Lofi," "Intense Rock," and an edge case called "Conflicting Vibe."

After increasing the weight of energy and reducing the importance of genre, the recommendations became more focused on matching intensity rather than category. For example, in the "High-Energy Pop" profile, songs like "Storm Runner" and "Neon Nights" ranked highly even though they are not pop songs, simply because their energy levels closely matched the user’s preference.

For the "Chill Lofi" profile, the system still performed well, with "Library Rain" and "Midnight Coding" ranking highest due to strong matches across all features. However, songs that only matched energy (but not genre or mood) began to appear more frequently in the top results.

The most noticeable issue appeared in the "Conflicting Vibe" profile. Even though the user specified a mood of "sad," none of the top recommendations reflected that mood. Instead, the system prioritized high-energy songs, showing that energy dominates the scoring logic and can override other important features.

Overall, the system became more consistent in matching energy but less accurate in capturing the full “vibe” of the user. This experiment demonstrates how increasing the weight of a single feature can reduce the system’s ability to balance multiple aspects of user preference.

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---
There are several ways this model could be improved. One improvement would be to add more songs and more diverse genres to reduce repetition and improve recommendation variety. Another improvement would be to balance feature weights more carefully so that no single feature (like energy) dominates the scoring system.

The model could also include additional user preferences, such as listening history or skip behavior, to make recommendations more personalized. Finally, adding a diversity rule in the ranking step could help ensure that the top results are not too similar to each other.

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

The biggest learning moment in this project was realizing how sensitive recommender systems are to feature weighting. Small changes, especially increasing the importance of energy, completely changed the ranking results and often outweighed genre or mood. This helped me understand that “intelligence” in these systems often comes from carefully tuned rules rather than complex logic.

Using AI tools like Copilot helped me quickly write and debug code, especially for functions like scoring and sorting songs. However, I had to double-check the AI’s suggestions when it came to how features were combined and weighted, because small mistakes or overly simplified logic could lead to unrealistic recommendations.

What surprised me most was how even a simple scoring system could feel like it was making meaningful recommendations. Even without machine learning, the combination of genre, mood, and energy was enough to produce results that felt personalized and realistic in many cases.

If I extended this project, I would add user interaction data such as likes, skips, or listening history to make the recommendations more dynamic. I would also try building a hybrid system that combines content-based filtering with collaborative filtering to better simulate real-world recommendation platforms.
