import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df['age'][df['sex'] == 'Male'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').sum() / df.shape[0] * 100, 1)

    # Advanced education (`Bachelors`, `Masters`, `Doctorate`)
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Percentage with salary >50K
    higher_education_rich = round((higher_education['salary'] == '>50K').sum() / higher_education.shape[0] * 100, 1)
    lower_education_rich = round((lower_education['salary'] == '>50K').sum() / lower_education.shape[0] * 100, 1)

    # Minimum number of hours a person works per week
    min_work_hours = df['hours-per-week'].min()

    # Percentage of rich among those who work fewest hours
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers['salary'] == '>50K').mean() * 100

    # Country with the highest percentage of people earning >50K
    country_earnings = df[df['salary'] == '>50K']['native-country'].value_counts() / df[
        'native-country'].value_counts() * 100
    highest_earning_country = country_earnings.idxmax()
    highest_earning_country_percentage = float(round(country_earnings.max(), 1))

    # Most popular occupation for those who earn >50K in India
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors:.1f}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich:.1f}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich:.1f}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage:.1f}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage:.1f}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
