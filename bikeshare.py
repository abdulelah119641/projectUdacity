import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

 # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("please enter the neme of city").lower().strip()
    while (city != "chicago" and city !="new york city" and city!= "washington"):
        city = input("Please select correct city among chicago, new york city or washington.").lower().strip()
        
    # TO DO: get user input for month (all, january, february, ... , june)    
    month = input("Which month would you like to filter by? January, February, March, April, May, June or type 'all' if you do not have any preference?").lower().strip()
    while(month != "january" and month!= "february" and month != "march" and month != "april" and month!= "may" and             month!= "june" and month != "All" ):
        month = input("plesse enter the month would you like to filter by? January, February, March, April, May, June or type 'all' if you do not have any preference?").strip()
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("wich day would you link to filter by? sunday , monday, tuesday, wednesday, thursday, friday, saturday, or all").lower().strip()
    while (day != "sunday" and day != "monday" and day != "tuesday" and day != "wednesday" and day != "thursday" and                day != "friday" and day !="saturday" and day != "all"):
        day = input("please enter the day would you link to by filter? sunday , monday, tuesday, wednesday, thursday, friday, saturday, or all")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
# now we will load the data for the city the user selected 
    df = pd.read_csv(CITY_DATA[city])
    
# now we will convert the start time to datatime

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # now we will extract the month, day, and houers
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    # now we will filter the data using month
    
    if month != "all":
        months = ['janury', 'february' , 'march' , 'april'  , 'may' , 'june']
        month = months.index(month)+1
        
        # now we will filter it 
        
        df = df[df['month'] == month]
        
        # now we will filter the month using day
        
        if day != "all": 
           # now we will filter it 
            df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    MostCommonMonth = df['month'].mode()[0]
    
    print("most common month it is " , MostCommonMonth ) 
    # TO DO: display the most common day of week
    MostCommonDay = df['day_of_week'].mode()[0]
    print("most common day it is" , MostCommonDay )
    # TO DO: display the most common start hour
    MostCommonHour = df['hour'].mode()[0] 
    print("most common hour it is" , MostCommonHour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    MostCommonlyUsedStart= df['Start Station'].mode()[0]
    print("The most commonly used start station it is" + MostCommonlyUsedStart)

    # TO DO: display most commonly used end station
    MostCommonlyUsedEnd= df['Start Station'].mode()[0]
    print("The most commonly used end start it is " + MostCommonlyUsedEnd)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " _" + df['End Station']
    FrequentCombination = df['combination'].mode()[0]
    print("The most frequent combibation of start station and end station  trip " + FrequentCombination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    TotalTravelTime = sum(df['Trip Duration'])
    TotalTravelTime = TotalTravelTime / 86400
    print("Total travel time it is" , TotalTravelTime)

    # TO DO: display mean travel time
    MeanTravelTime = df['Trip Duration'].mean()
    MeanTravelTime = MeanTravelTime/60
    print("The mean travel time" , MeanTravelTime)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df , city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    UserType = df.groupby(['User Type'])['User Type'].count()
    print("The user type it is " , UserType)

    # TO DO: Display counts of gender
    
    
    try:
        Gender = df.groupby(['Gender'])['Gender'].count()
        print("The Gender it is" , Gender)
    except KeyError: 
        print("sorry we don't have data for your selection in Gender")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        Earliest = sorted(df.groupby(['Birth Year'])['Birth Year'] , reverse=True)[0][0]
        print("the Most Earliest it is" , Earliest)
    except KeyError: 
        print("sorry we don't have data for your selection in Earliest")
    
    try:
        MostRecent = sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0]
        print("the Most Recent it is" , MostRecent)
    except KeyError: 
        print("sorry we don't have data for your selection in Most Recent")
    
    try:
        MostYear = df['Birth Year'].mode()
        print("the Most Year it is" , MostYear)
    except KeyError: 
        print("sorry we don't have data for your selection in Most Year")
        
    NumberOfRow = 1
    while True:
        data = input("\nWould you like to restart? Enter yes or no.\n").lower().strip()
        if data == "yes":
            print(df[NumberOfRow : NumberOfRow + 5])
            NumberOfRow = NumberOfRow + 5
        else:
              break
    
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df , city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
