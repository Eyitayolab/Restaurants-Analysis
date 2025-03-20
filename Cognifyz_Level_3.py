# Level 3, Task 1: Restaurant Reviews

# Description: Analyze the text reviews to identify the most common positive and negative keywords.
# Calculate the average length of reviews and explore if there is a relationship between review length and rating.

# The output should include the most common positive and negative keywords, the average length of reviews, and any insights on the relationship between review length and rating.

# Additionally, create visualizations to display the most common keywords and the relationship between review length and rating.

# Import necessary libraries for analysis
from collections import Counter
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Download NLTK data files (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

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

print("Starting Level 3, Task 1: Restaurant Reviews")  # Debug print

# Analyze the text reviews
with open("Level_3_Task_1_Output.txt", "w") as file:
    try:
        # Check if 'Review' column exists
        if 'Review' not in df.columns:
            file.write("The column 'Review' does not exist in the DataFrame. Skipping review analysis.\n")
        else:
            # Check for missing values in 'Review' and 'Aggregate rating' columns
            if df['Review'].isnull().any() or df['Aggregate rating'].isnull().any():
                raise KeyError("Missing values found in 'Review' or 'Aggregate rating' columns.")

            # Tokenize the reviews and remove stopwords
            stop_words = set(stopwords.words('english'))
            df['Review Tokens'] = df['Review'].apply(lambda x: [word for word in word_tokenize(x.lower()) if word.isalnum() and word not in stop_words])

            # Identify the most common positive and negative keywords
            positive_reviews = df[df['Aggregate rating'] >= 4]['Review Tokens'].sum()
            negative_reviews = df[df['Aggregate rating'] <= 2]['Review Tokens'].sum()

            positive_keywords = Counter(positive_reviews).most_common(10)
            negative_keywords = Counter(negative_reviews).most_common(10)

            file.write("\nMost Common Positive Keywords:\n")
            for word, count in positive_keywords:
                file.write(f"{word}: {count}\n")

            file.write("\nMost Common Negative Keywords:\n")
            for word, count in negative_keywords:
                file.write(f"{word}: {count}\n")

            # Calculate the average length of reviews
            df['Review Length'] = df['Review'].apply(len)
            average_review_length = df['Review Length'].mean()
            file.write(f"\nAverage Length of Reviews: {average_review_length:.2f} characters\n")

            # Explore the relationship between review length and rating
            plt.figure(figsize=(12, 8))
            sns.boxplot(x='Aggregate rating', y='Review Length', data=df)
            plt.title("Relationship Between Review Length and Rating", fontsize=16)
            plt.xlabel("Rating", fontsize=14)
            plt.ylabel("Review Length (characters)", fontsize=14)
            plt.xticks(fontsize=12)
            plt.yticks(fontsize=12)
            plt.grid(True)
            plt.savefig("Level_3_Task_1_Review_Length_vs_Rating.png")
            plt.show()

    except KeyError as e:
        file.write(f"Error: {e}\n")
    except Exception as e:
        file.write(f"An unexpected error occurred: {e}\n")

print("Finished Level 3, Task 1: Restaurant Reviews")  # Debug print

# Alternative Analysis: Sentiment Analysis on Rating Text and Votes
with open("Level_3_Task_1_Alternative_Analysis_Output.txt", "w") as file:
    try:
        # Check if 'Rating text' and 'Votes' columns exist
        if 'Rating text' not in df.columns or 'Votes' not in df.columns:
            raise KeyError("The required columns 'Rating text' or 'Votes' do not exist in the DataFrame.")

        # Map 'Rating text' to sentiment scores
        sentiment_mapping = {
            'Excellent': 5,
            'Very Good': 4,
            'Good': 3,
            'Average': 2,
            'Poor': 1
        }
        df['Sentiment Score'] = df['Rating text'].map(sentiment_mapping)

        # Calculate the average sentiment score
        average_sentiment_score = df['Sentiment Score'].mean()
        file.write(f"\nAverage Sentiment Score: {average_sentiment_score:.2f}\n")

        # Analyze the relationship between the number of votes and the aggregate rating
        plt.figure(figsize=(12, 8))
        sns.scatterplot(x='Votes', y='Aggregate rating', data=df)
        sns.regplot(x='Votes', y='Aggregate rating', data=df, scatter=False, color='red')
        plt.title("Relationship Between Number of Votes and Aggregate Rating", fontsize=16)
        plt.xlabel("Number of Votes", fontsize=14)
        plt.ylabel("Aggregate Rating", fontsize=14)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.grid(True)
        plt.savefig("Level_3_Task_1_Votes_vs_Rating.png")
        plt.show()

    except KeyError as e:
        file.write(f"Error: {e}\n")
    except Exception as e:
        file.write(f"An unexpected error occurred: {e}\n")

print("Finished Level 3, Task 1: Restaurant Reviews and Alternative Analysis")  # Debug print

# Level 3, Task 2: Votes Analysis

# Description: Identify the restaurants with the highest and lowest number of votes.
# Analyze if there is a correlation between the number of votes and the rating of a restaurant.

# The output should include the names of the restaurants with the highest and lowest number of votes, and any insights on the correlation between votes and rating.

# Additionally, create visualizations to display the correlation between votes and rating.

print("Starting Level 3, Task 2: Votes Analysis")  # Debug print

# Analyze the votes data
with open("Level_3_Task_2_Output.txt", "w") as file:
    try:
        # Check if 'Votes' and 'Aggregate rating' columns exist
        if 'Votes' not in df.columns or 'Aggregate rating' not in df.columns:
            raise KeyError("The required columns 'Votes' or 'Aggregate rating' do not exist in the DataFrame.")

        # Identify the restaurants with the highest and lowest number of votes
        highest_votes = df.loc[df['Votes'].idxmax()]
        lowest_votes = df.loc[df['Votes'].idxmin()]

        file.write(f"\nRestaurant with the highest number of votes:\n{highest_votes[['Restaurant Name', 'Votes', 'Aggregate rating']]}\n")
        file.write(f"\nRestaurant with the lowest number of votes:\n{lowest_votes[['Restaurant Name', 'Votes', 'Aggregate rating']]}\n")

        # Analyze the correlation between the number of votes and the rating
        correlation = df['Votes'].corr(df['Aggregate rating'])
        file.write(f"\nCorrelation between number of votes and aggregate rating: {correlation:.2f}\n")

        # Create a scatter plot with a regression line to visualize the correlation
        plt.figure(figsize=(12, 8))
        sns.scatterplot(x='Votes', y='Aggregate rating', data=df, alpha=0.5)
        sns.regplot(x='Votes', y='Aggregate rating', data=df, scatter=False, color='red')
        plt.title("Correlation Between Number of Votes and Aggregate Rating", fontsize=16)
        plt.xlabel("Number of Votes", fontsize=14)
        plt.ylabel("Aggregate Rating", fontsize=14)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.grid(True)
        plt.savefig("Level_3_Task_2_Votes_vs_Rating.png")
        plt.show()

    except KeyError as e:
        file.write(f"Error: {e}\n")
    except Exception as e:
        file.write(f"An unexpected error occurred: {e}\n")

print("Finished Level 3, Task 2: Votes Analysis")  # Debug print

# Level 3, Task 3: Price Range vs. Online Delivery and Table Booking

# Description: Analyze if there is a relationship between the price range and the availability of online delivery and table booking.
# Determine if higher-priced restaurants are more likely to offer these services.

# The output should include insights on the relationship between price range and the availability of online delivery and table booking.

# Additionally, create visualizations to display the relationship between price range and the availability of these services.

print("Starting Level 3, Task 3: Price Range vs. Online Delivery and Table Booking")  # Debug print

# Analyze the relationship between price range and the availability of online delivery and table booking
with open("Level_3_Task_3_Output.txt", "w") as file:
    try:
        # Check if 'Price range', 'Has Online delivery', and 'Has Table booking' columns exist
        if 'Price range' not in df.columns or 'Has Online delivery' not in df.columns or 'Has Table booking' not in df.columns:
            raise KeyError("The required columns 'Price range', 'Has Online delivery', or 'Has Table booking' do not exist in the DataFrame.")

        # Analyze the relationship between price range and online delivery
        online_delivery_by_price = df.groupby('Price range')['Has Online delivery'].value_counts(normalize=True).unstack().fillna(0) * 100
        file.write("\nOnline Delivery by Price Range (%):\n")
        file.write(f"{online_delivery_by_price}\n")

        # Analyze the relationship between price range and table booking
        table_booking_by_price = df.groupby('Price range')['Has Table booking'].value_counts(normalize=True).unstack().fillna(0) * 100
        file.write("\nTable Booking by Price Range (%):\n")
        file.write(f"{table_booking_by_price}\n")

        # Create a bar chart visualization for online delivery by price range
        online_delivery_by_price.plot(kind='bar', stacked=True, figsize=(12, 8), color=['red', 'green'])
        plt.title("Online Delivery by Price Range", fontsize=16)
        plt.xlabel("Price Range", fontsize=14)
        plt.ylabel("Percentage (%)", fontsize=14)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.legend(title='Online Delivery', labels=['No', 'Yes'], fontsize=12)
        plt.grid(True)
        plt.savefig("Level_3_Task_3_Online_Delivery_by_Price_Range.png")
        plt.show()

        # Create a bar chart visualization for table booking by price range
        table_booking_by_price.plot(kind='bar', stacked=True, figsize=(12, 8), color=['red', 'green'])
        plt.title("Table Booking by Price Range", fontsize=16)
        plt.xlabel("Price Range", fontsize=14)
        plt.ylabel("Percentage (%)", fontsize=14)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.legend(title='Table Booking', labels=['No', 'Yes'], fontsize=12)
        plt.grid(True)
        plt.savefig("Level_3_Task_3_Table_Booking_by_Price_Range.png")
        plt.show()

    except KeyError as e:
        file.write(f"Error: {e}\n")
    except Exception as e:
        file.write(f"An unexpected error occurred: {e}\n")

print("Finished Level 3, Task 3: Price Range vs. Online Delivery and Table Booking")  # Debug print

# Summary of Results

#### Level 3, Task 1: Restaurant Reviews and Alternative Analysis
# **Most Common Positive Keywords**: [List of keywords]
# **Most Common Negative Keywords**: [List of keywords]
# **Average Length of Reviews**: [Average length]
# **Average Sentiment Score**: 2.67
# **Relationship Between Number of Votes and Aggregate Rating**: A scatter plot with a regression line has been created to visualize this relationship.

#### Level 3, Task 2: Votes Analysis
# **Restaurant with the highest number of votes**: [Restaurant Name] (10,934 votes, Aggregate rating: 4.8)
# **Restaurant with the lowest number of votes**: [Restaurant Name] (0 votes, Aggregate rating: 0.0)
# **Correlation between number of votes and aggregate rating**: 0.31

#### Level 3, Task 3: Price Range vs. Online Delivery and Table Booking
# **Relationship Between Price Range and Online Delivery**: A bar chart has been created to visualize the percentage of restaurants offering online delivery by price range.
# **Relationship Between Price Range and Table Booking**: A bar chart has been created to visualize the percentage of restaurants offering table booking by price range.