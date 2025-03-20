# Level 1, Task 1: Top Cuisines

# Description: Analyze the dataset to find the top 3 cuisines in the city.

# The dataset contains information about restaurants in a city, including the type of cuisine they serve.

# The task is to identify the top 3 cuisines based on the number of restaurants serving that cuisine.

# The output should include the names of the top 3 cuisines, the number of restaurants serving each cuisine, and the percentage of restaurants serving each cuisine.

# Additionally, create a bar chart visualization to display the top 3 cuisines.

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Example code
print("Hello, Cognifyz Technologies!")

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

# Display the first few rows of the DataFrame
print(df.head())

# Print the column names to check the available columns
print(df.columns)

# Check for unique city names
unique_cities = df['City'].unique()
print("Unique city names:\n", unique_cities)

# Inspect rows where the city is 'Inner City'
inner_city_rows = df[df['City'] == 'Inner City']
print("Rows with 'Inner City':\n", inner_city_rows)

# Exclude 'Inner City' from the DataFrame
df = df[df['City'] != 'Inner City']

# Check for missing values in the 'Cuisines' column
if df['Cuisines'].isnull().any():
    print("Warning: There are missing values in the 'Cuisines' column. These rows will be excluded.")
    df = df.dropna(subset=['Cuisines'])

# Task 1: Top Cuisines
with open("Level_1_Task_1_Output.txt", "w") as file:
    try:
        cuisine_counts = df['Cuisines'].value_counts()
        top_3_cuisines = cuisine_counts[:3]
        total_restaurants = len(df)

        # Calculate the percentage of restaurants serving each of the top cuisine
        top_3_percentages = (top_3_cuisines / total_restaurants) * 100

        # Print the results neatly
        file.write("Top 3 Cuisines:\n")
        for cuisine, count, percentage in zip(top_3_cuisines.index, top_3_cuisines.values, top_3_percentages.values):
            file.write(f"{cuisine}: {count} restaurants ({percentage:.2f}%)\n")

        # Create a bar chart visualization
        plt.figure(figsize=(10, 6))
        sns.barplot(x=top_3_cuisines.index, y=top_3_cuisines.values, palette="viridis", hue=top_3_cuisines.index, dodge=False)
        plt.title("Top 3 Cuisines")
        plt.xlabel("Cuisine")
        plt.ylabel("Number of Restaurants")
        plt.legend([],[], frameon=False)

        # Add labels to the bars
        for index, value in enumerate(top_3_cuisines.values):
            plt.text(index, value, str(value), ha='center', va='bottom')

        plt.savefig("Level_1_Task_1_Top_3_Cuisines.png")
        plt.show()

    except KeyError:
        file.write('Error: The column "Cuisines" does not exist in the DataFrame.\n')
    except Exception as e:
        file.write(f"An unexpected error occurred while processing the data: {e}\n")

print("Finished Task 1: Top Cuisines")  # Debug print

# Task 2: City Analysis

# Description: Analyze the dataset to find the city with the most restaurants and the city with the highest average rating.

# The task is to analyze the number of restaurants and the average aggregate ratings per city.

# The output should include the city with the most restaurants, the city with the highest average rating, and the corresponding values.

# Additionally, create bar chart visualizations to display the number of restaurants in each city and the average ratings per city.

print("Starting Task 2: City Analysis")  # Debug print

# Analyze the number of restaurants and average aggregate ratings per city
with open("Level_1_Task_2_Output.txt", "w") as file:
    try:
        # Check for missing values in 'City' and 'Aggregate rating' columns
        if df['City'].isnull().any() or df['Aggregate rating'].isnull().any():
            raise KeyError("Missing values found in 'City' or 'Aggregate rating' columns.")

        # Debug prints to check the data
        print("City column data:\n", df['City'].head())
        print("Aggregate rating column data:\n", df['Aggregate rating'].head())

        # Count the number of restaurants in each city
        city_counts = df['City'].value_counts()
        print("City counts:\n", city_counts)  # Debug print
    
        # Identify the city with the highest number of restaurants
        city_most_restaurants = city_counts.idxmax()
        print("City with most restaurants:", city_most_restaurants)  # Debug print

        # Calculate the average rating for restaurants in each city
        average_ratings = df.groupby('City')['Aggregate rating'].mean()
        print("Average ratings:\n", average_ratings)  # Debug print
    
        # Identify the city with the highest average rating
        city_highest_rating = average_ratings.idxmax()
        print("City with highest average rating:", city_highest_rating)  # Debug print

        # Print the results neatly
        file.write(f"City with most restaurants: {city_most_restaurants}\n")
        file.write(f"City with highest average rating: {city_highest_rating}\n")

        # Create a bar chart visualization for the number of restaurants in each city
        plt.figure(figsize=(14, 8))
        sns.barplot(x=city_counts.index[:10], y=city_counts.values[:10], palette="viridis", hue=city_counts.index[:10], dodge=False)
        plt.title("Top 10 Cities with Most Restaurants")
        plt.xlabel("City")
        plt.ylabel("Number of Restaurants")
        plt.xticks(rotation=45)
        plt.legend([],[], frameon=False)
        plt.savefig("Level_1_Task_2_Top_10_Cities_Most_Restaurants.png")
        plt.show()

        # Create a bar chart visualization for the average ratings per city
        plt.figure(figsize=(14, 8))
        sns.barplot(x=average_ratings.index[:10], y=average_ratings.values[:10], palette="viridis", hue=average_ratings.index[:10], dodge=False)
        plt.title("Top 10 Cities with Highest Average Ratings")
        plt.xlabel("City")
        plt.ylabel("Average Rating")
        plt.xticks(rotation=45)
        plt.legend([],[], frameon=False)
        plt.savefig("Level_1_Task_2_Top_10_Cities_Highest_Average_Ratings.png")
        plt.show()

    except KeyError as e:
        file.write(f"Error: {e}\n")
    except Exception as e:
        file.write(f"An unexpected error occurred: {e}\n")

print("Finished Task 2: City Analysis")  # Debug print

# Task 3: Price Range Distribution

# Description: Analyze the dataset to find the distribution of restaurants across different price ranges.

# The task is to analyze the number of restaurants in each price range and calculate the percentage of restaurants in each price range.

# The output should include the number of restaurants and the percentage of restaurants in each price range.

# Additionally, create a bar chart visualization to display the price range distribution.

print("Starting Task 3: Price Range Distribution")  # Debug print

# Analyze the distribution of restaurants across different price ranges
with open("Level_1_Task_3_Output.txt", "w") as file:
    try:
        # Check for missing values in 'Price range' column
        if df['Price range'].isnull().any():
            raise KeyError("Missing values found in 'Price range' column.")

        # Count the number of restaurants in each price range
        price_range_counts = df['Price range'].value_counts()
        total_restaurants = len(df)
        price_range_percentages = (price_range_counts / total_restaurants) * 100
        print("Price range counts:\n", price_range_counts)  # Debug print

        # Define price range descriptions
        price_range_descriptions = {
            1: "Low cost ($)",
            2: "Moderate cost ($$)",
            3: "High cost ($$$)",
            4: "Very high cost ($$$$)"
        }
    
        # Print the results neatly
        file.write("Price Range Distribution:\n")
        for price_range, count, percentage in zip(price_range_counts.index, price_range_counts.values, price_range_percentages.values):
            description = price_range_descriptions.get(price_range, f"Price Range {price_range}")
            file.write(f"{description}: {count} restaurants ({percentage:.2f}%)\n")
    
        # Create a bar chart visualization for the price range distribution
        plt.figure(figsize=(10, 6))
        sns.barplot(x=price_range_counts.index.astype(str), y=price_range_counts.values, palette="viridis", hue=price_range_counts.index.astype(str), dodge=False)
        plt.title("Price Range Distribution")
        plt.xlabel("Price Range")
        plt.ylabel("Number of Restaurants")
        plt.xticks(rotation=45)
        plt.legend([],[], frameon=False)
        plt.savefig("Level_1_Task_3_Price_Range_Distribution.png")
        plt.show()

    except KeyError as e:
        file.write(f"Error: {e}\n")
    except Exception as e:
        file.write(f"An unexpected error occurred: {e}\n")

print("Finished Task 3: Price Range Distribution")  # Debug print

# Task 4: Online Delivery Analysis

# Description: Analyze the dataset to find the percentage of restaurants offering online delivery and compare the average ratings of restaurants with and without online delivery.

# The task is to analyze the distribution of restaurants based on whether they offer online delivery and compare the average ratings of restaurants with and without online delivery.

# The output should include the percentage of restaurants offering online delivery, the average ratings of restaurants with and without online delivery, and a bar chart visualization for the online delivery distribution and average ratings by online delivery status.

# Additionally, create a bar chart visualization to display the average ratings by online delivery status.

print("Starting Task 4: Online Delivery Analysis")  # Debug print

# Analyze the percentage of restaurants offering online delivery and compare the average ratings of restaurants with and without online delivery
with open("Level_1_Task_4_Output.txt", "w") as file:
    try:
        # Check for missing values in 'Has Online delivery' and 'Aggregate rating' columns
        if df['Has Online delivery'].isnull().any() or df['Aggregate rating'].isnull().any():
            raise KeyError("Missing values found in 'Has Online delivery' or 'Aggregate rating' columns.")

        # Calculate the percentage of restaurants offering online delivery
        online_delivery_counts = df['Has Online delivery'].value_counts()
        total_restaurants = len(df)
        online_delivery_percentages = (online_delivery_counts / total_restaurants) * 100
        print("Online delivery counts:\n", online_delivery_counts)  # Debug print

        # Print the results neatly
        file.write("Online Delivery Distributions:\n")
        for delivery_status, count, percentage in zip(online_delivery_counts.index, online_delivery_counts.values, online_delivery_percentages.values):
            status = "Offers Online Delivery" if delivery_status == 'Yes' else "Does Not offer Online Delivery"
            file.write(f"{status}: {count} restaurants ({percentage:.2f}%)\n")
        
        # Compare the average ratings of restaurants with and without online delivery
        average_ratings_online_delivery = df.groupby('Has Online delivery')['Aggregate rating'].mean()
        file.write("\nAverage Ratings by Online Delivery Status:\n")
        for delivery_status, avg_rating in average_ratings_online_delivery.items():
            status = "Offers Online Delivery" if delivery_status == 'Yes' else "Does Not Offer Online Delivery"
            file.write(f"{status}: {avg_rating:.2f}\n")

        # Create a bar chart visualization for the online delivery distribution
        plt.figure(figsize=(10, 6))
        sns.barplot(x=online_delivery_counts.index.astype(str), y=online_delivery_counts.values, palette="viridis", hue=online_delivery_counts.index.astype(str), dodge=False)
        plt.title("Online Delivery Distribution")
        plt.xlabel("Online Delivery Status")
        plt.ylabel("Number of Restaurants")
        plt.xticks(rotation=45)
        plt.legend([],[], frameon=False)
        plt.savefig("Level_1_Task_4_Online_Delivery_Distribution.png")
        plt.savefig("Level_1_Task_4_Average_Ratings_Online_Delivery_Status.png")
        plt.show()

        # Create a bar chart visualization for the average ratings by online delivery status
        plt.figure(figsize=(10, 6))
        sns.barplot(x=average_ratings_online_delivery.index.astype(str), y=average_ratings_online_delivery.values, palette="viridis", hue=average_ratings_online_delivery.index.astype(str), dodge=False)
        plt.title("Average Ratings by Online Delivery Status")
        plt.xlabel("Online Delivery Status")
        plt.ylabel("Average Rating")
        plt.xticks(rotation=45)
        plt.legend([],[], frameon=False)
        plt.show()

    except KeyError as e:
        file.write(f"Error: {e}\n")
    except Exception as e:
        file.write(f"An unexpected error occurred: {e}\n")

print("Finished Task 4: Online Delivery Analysis")  # Debug print

# Summary of Results

#### Task 1: Top 3 Cuisines
# 1. **North Indian**: 936 restaurants (9.80%)
# 2. **North Indian, Chinese**: 511 restaurants (5.35%)
# 3. **Fast Food**: 354 restaurants (3.71%)

#### Task 2: City Analysis
# **City with most restaurants**: New Delhi
# **City with highest average rating**: Quezon City

#### Task 3: Price Range Distribution
# **Low cost ($)**: 4444 restaurants (46.54%)
# **Moderate cost ($$)**: 3113 restaurants (32.60%)
# **High cost ($$$)**: 1408 restaurants (14.74%)
# **Very high cost ($$$$)**: 584 restaurants (6.12%)

#### Task 4: Online Delivery Analysis
# **Offers Online Delivery**: 2451 restaurants (25.67%)
# **Does Not Offer Online Delivery**: 7098 restaurants (74.33%)
# **Average Rating for Restaurants Offering Online Delivery**: 3.25
# **Average Rating for Restaurants Not Offering Online Delivery**: 2.46∏