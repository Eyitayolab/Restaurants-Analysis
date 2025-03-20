# Restaurants-Analysis

# Restaurant Data Analysis Project

This project analyzes a restaurant dataset to extract insights into restaurant ratings, cuisine preferences, geographic distribution, service availability, and customer sentiment.

## Table of Contents

- [Project Description](#project-description)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Findings](#findings)
- [Problems Encountered](#problems-encountered)
- [Recommendations](#recommendations)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Project Description

This project consists of three levels of analysis:

-   **Level 1:** Basic data exploration, cleaning, and initial visualizations.
-   **Level 2:** Advanced statistical analysis, geographic clustering, and restaurant chain analysis.
-   **Level 3:** Text analysis (sentiment), correlation analysis, and service availability analysis.

The goal is to provide actionable insights for restaurants and to demonstrate data analysis skills.

## Dataset

The dataset used is `cognifyz_dataset.csv`. It contains information about restaurants, including ratings, cuisine types, locations, and other relevant features.

## Project Structure

Restaurant-Data-Analysis/
├── data/
│   └── cognifyz_dataset.csv
├── level1/
│   ├── level1_analysis.py
│   ├── level1_task1_output.txt
│   ├── level1_task2_output.txt
│   ├── level1_task3_output.txt
│   ├── level1_task4_output.txt
│   ├── level1_task1_top_3_cuisines.png
│   ├── level1_task2_top_10_cities_most_restaurants.png
│   ├── level1_task2_top_10_cities_highest_average_ratings.png
│   ├── level1_task3_price_range_distribution.png
│   ├── level1_task4_online_delivery_distribution.png
│   └── level1_task4_average_ratings_online_delivery_status.png
├── level2/
│   ├── level2_analysis.py
│   ├── level2_task1_output.txt
│   ├── level2_task1_rating_distribution.png
│   ├── level2_task2_output.txt
│   ├── level2_task2_top_10_cuisine_combinations.png
│   ├── level2_task2_average_ratings_top_10_cuisine_combinations.png
│   ├── level2_task3_output.txt
│   ├── level2_task3_restaurant_map.html
│   ├── level2_task4_output.txt
│   ├── level2_task4_average_ratings_top_10_restaurant_chains.png
│   └── level2_task4_popularity_top_10_restaurant_chains.png
├── level3/
│   ├── level3_analysis.py
│   ├── level3_task1_output.txt
│   ├── level3_task1_alternative_analysis_output.txt
│   ├── level3_task1_review_length_vs_rating.png
│   ├── level3_task1_votes_vs_rating.png
│   ├── level3_task2_output.txt
│   ├── level3_task2_votes_vs_rating.png
│   ├── level3_task3_output.txt
│   ├── level3_task3_online_delivery_by_price_range.png
│   └── level3_task3_table_booking_by_price_range.png
├── README.md
├── requirements.txt

## Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/Eyitayolab/Restaurants-Analysis.git
    ```

2.  Navigate to the project directory:

    ```bash
    cd Restaurant-Data-Analysis
    ```

3.  Create a virtual environment (recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

4.  Install the required libraries:

    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn folium nltk
    ```

5.  Download NLTK data:

    ```bash
    python3 -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
    ```

## Usage

1.  Run the Python scripts for each level:

    ```bash
   python3 level1/level1_analysis.py
python3 level2/level2_analysis.py
python3 level3/level3_analysis.py
    ```

2.  View the visualizations in the level folders

## Findings

-   **Rating and Votes Correlation:**
    -      A moderate positive correlation (0.31) was observed between restaurant aggregate ratings and the number of votes. This suggests that restaurants with higher ratings tend to receive more votes, indicating a relationship between customer satisfaction and engagement.
    -   ![Votes vs. Rating](level3/level3_task2_votes_vs_rating.png)
-   **Geographic Clustering:**
    -      DBSCAN clustering revealed distinct geographic clusters of restaurants. Some clusters exhibited significantly higher average ratings (e.g., Cluster 0 with an average rating of 4.66), while others had notably lower ratings (e.g., Cluster 66 with an average rating of 0.23). This highlights the influence of location on restaurant performance.
    -   The largest clusters were cluster 64, 45, and 47, showing high concentrations of restaurants in those areas.
    -   ![Restaurant Clusters](level2/level2_task3_restaurant_map.png)
-   **Cuisine Preferences:**
    -      "North Indian" and "North Indian, Chinese" were the most common cuisine combinations. However, average ratings varied significantly. "Barbeque Nation" restaurants had the highest average rating among the top 10 chains (4.35), while "Baskin Robbins" had the lowest (1.86).
    -   ![Top 10 Cuisine Combinations](level2/level2_task2_top_10_cuisine_combinations.png)
-   **Service Availability:**
    -      Higher-priced restaurants were more likely to offer online delivery and table booking services. Price range 4 had the highest percentage of restaurants that offered both services.
    -   ![Online Delivery by Price Range](level3/level3_task3_online_delivery_by_price_range.png)
    -   ![Table Booking by Price Range](level3/level3_task3_table_booking_by_price_range.png)
-   **Sentiment Analysis:**
    -      The average sentiment score based on rating text was 2.67, indicating a slightly positive overall sentiment. The relationship between vote count and aggregate rating, visualized through a scatter plot with a regression line, showed a trend of higher ratings with increased votes.
    -   ![Review length vs rating](level3/level3_task1_review_length_vs_rating.png)
-   **Restaurant Chains:**
    -   Cafe Coffee Day had the most locations, but McDonalds and Pizza Hut had higher average ratings, and Pizza hut and Barbeque Nation had the highest average vote counts.
    -   ![Average Ratings of Top 10 Restaurant Chains](level2/level2_task4_average_ratings_top_10_restaurant_chains.png)
    -   ![Popularity (Average Votes) of Top 10 Restaurant Chains](level2/level2_task4_popularity_top_10_restaurant_chains.png)

## Problems Encountered

-   **Missing "Review" Column:** The absence of the "Review" column in the Level 3 dataset necessitated a change in analysis strategy.
-   **Data Cleaning:** Initial data cleaning was required to handle missing values and inconsistencies.

## Recommendations

-   **Enhance Customer Engagement:**
    -      Given the correlation between ratings and votes, restaurants should implement strategies to encourage customer reviews and feedback. This could include loyalty programs, post-dining surveys, or social media engagement.
-   **Location-Based Strategies:**
    -      Restaurants should leverage geographic insights to tailor their services and marketing. For example:
        -      In high-rated clusters, focus on maintaining quality and enhancing customer experience to retain positive reviews.
        -      In low-rated clusters, investigate potential issues (e.g., service quality, food consistency) and implement corrective measures.
        -   Utilize location data to target promotions and advertising to specific areas.
-   **Cuisine and Chain Optimization:**
    -      Restaurants should analyze cuisine preferences and chain performance to optimize their menus and branding. Consider:
        -      Introducing popular cuisine combinations or dishes based on regional preferences.
        -      Benchmarking performance against successful chains like "Barbeque Nation" to identify best practices.
-   **Service Customization:**
    -      Tailor online delivery and table booking services to align with the preferences of customers in different price ranges. For example:
        -      Offer premium delivery options or exclusive table booking perks for higher-priced restaurants.
        -      Ensure efficient and reliable basic services for lower-priced restaurants.
-   **Continuous Sentiment Monitoring:**
    -      Even with limited review data, regularly monitor customer sentiment based on rating text. Use this feedback to identify areas for improvement and maintain high ratings.
-   **Data Completeness:**
    -   Future data collection should focus on including the review column, to allow for more in depth sentiment analysis.
-   **Vote Analysis:**
    -   Investigate why some restaurants have a high vote count, and some have low. This may show what customers are interested in.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the Copyright © 2024 Seun Ojo License.

## Author

Seun Ojo
(https://github.com/Eyitayolab)