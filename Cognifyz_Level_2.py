# Level 2, Task 1: Restaurant Ratings

# Description: Analyze the dataset to find the distribution of aggregate restaurant ratings, determine the most common rating range and calculate the average number of votes received by restaurants in each rating range.

# The task is to analyze the distribution of aggregate ratings for restaurants, identify the most common rating range, and calculate the average number of votes received by restaurants in each rating range.

# The output should include the most common rating range, the average number of votes received by restaurants in each rating range, and a histogram visualization for the rating distribution.

# Additionally, create a histogram visualization to display the rating distribution.

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from sklearn.cluster import DBSCAN
import numpy as np

# Load the dataset into a DataFrame
try:
    df = pd.read_csv("cognifyz_dataset.csv")
except FileNotFoundError:
    print("Error: The file 'cognifyz_dataset.csv' was not found.")
    exit(1)
except pd.errors.EmptyDataError:
    print("Error: The file 'cognifyz_dataset.csv' is empty.")
    exit(1)
except pd.errors.ParserError:
    print("Error: The file 'cognifyz_dataset.csv' could not be parsed.")
    exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit(1)

print("Starting Level 2, Task 1: Restaurant Ratings")  # Debug print

# Analyze the distribution of aggregate restaurant ratings, determine the most common rating range, and calculate the average number of votes received by restaurants in each rating range

# Task 1: Restaurant Ratings
with open("Level_2_Task_1_Output.txt", "w") as file:
    try:
        # Calculate rating statistics
        rating_stats = df['Aggregate rating'].describe()
        file.write("\nAggregate Rating Statistics:\n")
        file.write(f"{rating_stats}\n")

        # Determine most common rating range
        rating_ranges = pd.cut(df['Aggregate rating'], bins=[0, 1, 2, 3, 4, 5])
        most_common_rating_range = rating_ranges.value_counts().idxmax()
        file.write(f"\nMost common rating range: {most_common_rating_range}\n")

        # Calculate average votes
        average_votes_by_rating_range = df.groupby(rating_ranges, observed=False)['Votes'].mean()
        file.write("\nAverage number of votes by rating range:\n")
        for rating_range, avg_votes in average_votes_by_rating_range.items():
            file.write(f"{rating_range}: {avg_votes:.2f}\n")

        # Analyze rating distribution
        plt.figure(figsize=(8, 6))
        sns.histplot(df['Aggregate rating'], kde=True)
        plt.title("Distribution of Aggregate Ratings", fontsize=16)
        plt.xlabel("Aggregate Rating", fontsize=14)
        plt.ylabel("Frequency", fontsize=14)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.grid(True)

        # Add a vertical line to highlight the most common rating range
        plt.axvline(x=most_common_rating_range.left + 0.5, color='red', linestyle='--', linewidth=2, label='Most Common Rating Range')

        # Annotate the most common rating range
        plt.annotate(f'Most common rating range: {most_common_rating_range}', 
                     xy=(most_common_rating_range.left + 0.5, 0), 
                     xytext=(most_common_rating_range.left + 0.5, 10),
                     arrowprops=dict(facecolor='black', shrink=0.05),
                     fontsize=12, ha='center')
        
        # Add legend
        plt.legend()
        
        plt.savefig("Level_2_Task_1_Rating_Distribution.png")
        plt.show()

    except KeyError:
        file.write("Error: One or more required columns ('Aggregate rating', 'Votes') are missing.\n")
    except Exception as e:
        file.write(f"An unexpected error occurred: {e}\n")

print("Finished Level 2, Task 1: Restaurant Ratings")  # Debug print

# Level 2, Task 2: Cuisine Combination

# Description: Analyze the dataset to identify the most common cuisine combinations and determine if certain cuisine combinations tend to higher ratings.

# The task is to analyze the cuisine combinations in the dataset, identify the most common cuisine combinations, and determine if certain cuisine combinations tend to receive higher ratings.

# The output should include the most common cuisine combinations, the average ratings for the top cuisine combinations, and a bar chart visualization for the average ratings by cuisine combination.

# Additionally, create a bar chart visualization to display the average ratings by cuisine combination.

print("Starting Level 2, Task 2: Cuisine Combination")  # Debug print

# Analyze the cuisine combinations in the dataset, identify the most common cuisine combinations, and determine if certain cuisine combinations tend to receive higher ratings

# Task 2: Cuisine Combination
with open("Level_2_Task_2_Output.txt", "w") as file:
    try:
        # Identify the most common cuisine combinations
        cuisine_combinations = df['Cuisines'].value_counts()
        top_cuisine_combinations = cuisine_combinations[:10]
        file.write("\nTop 10 Cuisine Combinations:\n")
        for combination, count in zip(top_cuisine_combinations.index, top_cuisine_combinations.values):
            file.write(f"{combination}: {count} restaurants\n")

        # Calculate the average ratings for each cuisine combination
        average_ratings_by_combination = df.groupby('Cuisines')['Aggregate rating'].mean()
        top_average_ratings = average_ratings_by_combination[top_cuisine_combinations.index]
        file.write("\nAverage Ratings for Top 10 Cuisine Combinations:\n")
        for combination, avg_rating in zip(top_average_ratings.index, top_average_ratings.values):
            file.write(f"{combination}: {avg_rating:.2f}\n")

        # Create a bar chart visualization for the frequency of top cuisine combinations
        plt.figure(figsize=(12, 8))
        sns.barplot(x=top_cuisine_combinations.index, y=top_cuisine_combinations.values, hue=top_cuisine_combinations.index, palette="viridis", dodge=False, legend=False)
        plt.title("Frequency of Top 10 Cuisine Combinations", fontsize=16)
        plt.xlabel("Cuisine Combination", fontsize=14)
        plt.ylabel("Number of Restaurants", fontsize=14)
        plt.xticks(rotation=45, fontsize=12, ha='right')
        plt.yticks(fontsize=12)
        plt.grid(True)
        plt.savefig("Level_2_Task_2_Top_10_Cuisine_Combinations.png")
        plt.show() 

        # Create a bar chart visualization for the average ratings by cuisine combination
        plt.figure(figsize=(12, 8))
        sns.barplot(x=top_average_ratings.index, y=top_average_ratings.values, hue=top_average_ratings.index, palette="viridis", dodge=False, legend=False)
        plt.title("Average Ratings by Top 10 Cuisine Combinations", fontsize=16)
        plt.xlabel("Cuisine Combination", fontsize=14)
        plt.ylabel("Average Rating", fontsize=14)
        plt.xticks(rotation=45, fontsize=12, ha='right')
        plt.yticks(fontsize=12)
        plt.grid(True)
        plt.savefig("Level_2_Task_2_Average_Ratings_Top_10_Cuisine_Combinations.png")
        plt.show()

    except KeyError as e:
        file.write(f"Error: {e}\n")
    except Exception as e:
        file.write(f"An unexpected error occurred: {e}\n")

print("Finished Level 2, Task 2: Cuisine Combination")  # Debug print

# Level 2, Task 3: Geographic Analysis

# Description: Analyze the dataset to identify the geographic distribution of restaurants on a map using longitude and latitude coordinates and determine if there are any patterns or clusters based on location.

# The task is to analyze the geographic distribution of restaurants based on their longitude and latitude coordinates, identify any patterns or clusters based on location, and visualize the distribution on a map.

# The output should include a map visualization showing the geographic distribution of restaurants and any identified patterns or clusters.

# Additionally, create a map visualization to display the geographic distribution of restaurants.

print("Starting Level 2, Task 3: Geographic Analysis")  # Debug print

# Plot the locations of restaurants on a map using longitude and latitude coordinates

# Task 3: Geographic Analysis
with open("Level_2_Task_3_Output.txt", "w") as file:
    try:
        # Extract longitude and latitude
        locations = df[['Longitude', 'Latitude']].dropna()

        # Create a map centered around the mean latitude and longitude
        map_center = [locations['Latitude'].mean(), locations['Longitude'].mean()]
        restaurant_map = folium.Map(location=map_center, zoom_start=12)

        # Add points to the map
        for _, row in locations.iterrows():
            folium.Marker([row['Latitude'], row['Longitude']]).add_to(restaurant_map)

        # Save the map to an HTML file
        restaurant_map.save("Level_2_Task_3_Restaurant_Map.html")

        # Perform clustering using DBSCAN
        db = DBSCAN(eps=0.01, min_samples=10).fit(locations)
        labels = db.labels_

        # Add cluster labels to the DataFrame
        df['Cluster'] = labels

        # Calculate the number of restaurants in each cluster
        cluster_counts = df['Cluster'].value_counts()
        file.write("\nCluster Summary:\n")
        file.write(f"{cluster_counts}\n")

        # Calculate the average rating for each cluster
        average_ratings_by_cluster = df.groupby('Cluster')['Aggregate rating'].mean()
        file.write("\nAverage Ratings by Cluster:\n")
        for cluster, avg_rating in average_ratings_by_cluster.items():
            file.write(f"Cluster {cluster}: {avg_rating:.2f}\n")

    except KeyError as e:
        file.write(f"Error: {e}\n")
    except Exception as e:
        file.write(f"An unexpected error occurred: {e}\n")

print("Finished Level 2, Task 3: Geographic Analysis")  # Debug print

# Level 2, Task 4: Restaurant Chains

# Description: Identify if there are any restaurant chains present in the dataset and analyze the ratings and popularity of different restaurant chains.

# The task is to identify restaurant chains, analyze their ratings and popularity, and create visualizations to display the results.

# The output should include the names of the restaurant chains, the number of restaurants in each chain, the average ratings for each chain, and visualizations for the popularity and ratings of the chains.

# Additionally, create bar chart visualizations to display the average ratings and popularity of restaurant chains.

print("Starting Level 2, Task 4: Restaurant Chains")  # Debug print

# Identify restaurant chains and analyze their ratings and popularity

# Task 4: Restaurant Chains
with open("Level_2_Task_4_Output.txt", "w") as file:
    try:
        # Check for missing values in 'Restaurant Name' and 'Aggregate rating' columns
        if df['Restaurant Name'].isnull().any() or df['Aggregate rating'].isnull().any():
            raise KeyError("Missing values found in 'Restaurant Name' or 'Aggregate rating' columns.")

        # Identify restaurant chains by grouping by 'Restaurant Name' and counting the occurrences
        restaurant_chains = df['Restaurant Name'].value_counts()
        chains = restaurant_chains[restaurant_chains > 1]
        file.write("\nRestaurant Chains:\n")
        file.write(f"{chains}\n")

        # Analyze the ratings and popularity of different restaurant chains
        chain_ratings = df[df['Restaurant Name'].isin(chains.index)].groupby('Restaurant Name')['Aggregate rating'].mean()
        chain_popularity = df[df['Restaurant Name'].isin(chains.index)].groupby('Restaurant Name')['Votes'].mean()

        # Limit to top 10 restaurant chains based on the number of restaurants
        top_chains = chains[:10].index
        top_chain_ratings = chain_ratings[top_chains]
        top_chain_popularity = chain_popularity[top_chains]
       
        # Print the results neatly
        file.write("\nAverage Ratings for Top 10 Restaurant Chains:\n")
        for chain, avg_rating in top_chain_ratings.items():
            file.write(f"{chain}: {avg_rating:.2f}\n")

        file.write("\nPopularity (Average Votes) for Top 10 Restaurant Chains:\n")
        for chain, avg_votes in top_chain_popularity.items():
            file.write(f"{chain}: {avg_votes:.2f}\n")

        # Create a bar chart visualization for the average ratings of restaurant chains
        plt.figure(figsize=(14, 8))
        sns.barplot(x=top_chain_ratings.index, y=top_chain_ratings.values, hue=top_chain_ratings.index, palette="viridis", dodge=False, legend=False)
        plt.title("Average Ratings of Top 10 Restaurant Chains")
        plt.xlabel("Restaurant Chain")
        plt.ylabel("Average Rating")
        plt.xticks(rotation=45)
        plt.savefig("Level_2_Task_4_Average_Ratings_Top_10_Restaurant_Chains.png")
        plt.show()

        # Create a bar chart visualization for the popularity (average votes) of restaurant chains
        plt.figure(figsize=(14, 8))
        sns.barplot(x=top_chain_popularity.index, y=top_chain_popularity.values, hue=top_chain_popularity.index, palette="viridis", dodge=False, legend=False)
        plt.title("Popularity (Average Votes) of Top 10 Restaurant Chains")
        plt.xlabel("Restaurant Chain")
        plt.ylabel("Average Votes")
        plt.xticks(rotation=45)
        plt.savefig("Level_2_Task_4_Popularity_Top_10_Restaurant_Chains.png")
        plt.show()

    except KeyError as e:
        file.write(f"Error: {e}\n")
    except Exception as e:
        file.write(f"An unexpected error occurred: {e}\n")

print("Finished Level 2, Task 4: Restaurant Chains")  # Debug print

# Summary of Results

#### Level 2, Task 1: Restaurant Ratings
# **Most common rating range**: (3, 4]
# **Average number of votes by rating range**:
# 1. (0, 1]: nan
# 2. (1, 2]: 144.20
# 3. (2, 3]: 38.99
# 4. (3, 4]: 162.15
# 5. (4, 5]: 637.99

#### Level 2, Task 2: Cuisine Combination
# **Top 10 Cuisine Combinations**:
# 1. North Indian: 936 restaurants
# 2. North Indian, Chinese: 511 restaurants
# 3. Fast Food: 354 restaurants
# 4. Chinese: 354 restaurants
# 5. North Indian, Mughlai: 334 restaurants
# 6. Cafe: 299 restaurants
# 7. Bakery: 218 restaurants
# 8. North Indian, Mughlai, Chinese: 197 restaurants
# 9. Bakery, Desserts: 170 restaurants
# 10. Street Food: 149 restaurants

# **Average Ratings for Top 10 Cuisine Combinations**:
# 1. North Indian: 1.67
# 2. North Indian, Chinese: 2.42
# 3. Fast Food: 2.12
# 4. Chinese: 2.04
# 5. North Indian, Mughlai: 2.89
# 6. Cafe: 2.89
# 7. Bakery: 1.92
# 8. North Indian, Mughlai, Chinese: 2.57
# 9. Bakery, Desserts: 2.32
# 10. Street Food: 2.16

#### Level 2, Task 3: Geographic Analysis
# **Map has been created and saved as 'cognifyzrestaurant_map.html'.**

# **Cluster Summary**:
# - **Largest Clusters**:
#   - Cluster 64: 4150 restaurants
#   - Cluster 45: 1630 restaurants
#   - Cluster 47: 1008 restaurants
#   - Cluster 23: 497 restaurants
#   - Cluster 65: 106 restaurants
# - **Noise (No Cluster)**: 935 restaurants

# **Average Ratings by Cluster**:
# - **Highest Rated Clusters**:
#   - Cluster 0: 4.66
#   - Cluster 50: 4.39
#   - Cluster 55: 4.34
#   - Cluster 30: 4.42
#   - Cluster 95: 4.36
# - **Lowest Rated Clusters**:
#   - Cluster 66: 0.23
#   - Cluster 67: 0.16
#   - Cluster 68: 0.06
#   - Cluster 69: 0.00
#   - Cluster 70: 0.00

#### Level 2, Task 4: Restaurant Chains
# **Top 10 Restaurant Chains**:
# 1. Cafe Coffee Day: 83 restaurants
# 2. Domino's Pizza: 79 restaurants
# 3. Subway: 63 restaurants
# 4. Green Chick Chop: 51 restaurants
# 5. McDonald's: 48 restaurants
# 6. Keventers: 44 restaurants
# 7. Pizza Hut: 41 restaurants
# 8. Giani: 39 restaurants
# 9. Baskin Robbins: 35 restaurants
# 10. Barbeque Nation: 31 restaurants

# **Average Ratings for Top 10 Restaurant Chains**:
# 1. Cafe Coffee Day: 2.42
# 2. Domino's Pizza: 2.74
# 3. Subway: 2.91
# 4. Green Chick Chop: 2.67
# 5. McDonald's: 3.34
# 6. Keventers: 2.87
# 7. Pizza Hut: 3.32
# 8. Giani: 2.69
# 9. Baskin Robbins: 1.86
# 10. Barbeque Nation: 4.35

# **Popularity (Average Votes) for Top 10 Restaurant Chains**:
# 1. Cafe Coffee Day: 29.25
# 2. Domino's Pizza: 84.09
# 3. Subway: 97.21
# 4. Green Chick Chop: 18.90
# 5. McDonald's: 110.23
# 6. Keventers: 37.15
# 7. Pizza Hut: 165.37
# 8. Giani: 29.45
# 9. Baskin Robbins: 15.29
# 10. Barbeque Nation: 1082.38