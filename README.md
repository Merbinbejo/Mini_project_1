# Mini_project_1
Game Analytics: Unlocking Tennis Data with SportRadar API
extracting JSON data from sportradar API using python code with API key and visulizing the data using JSON library
inserting the extracted json data from the Tennis data API, creating tables and inserting the data using the library mysql-connector.
Created table and data inserted:
        1.category 
        2.competitions
        3.competitors
        4.competitor_rankings
        5.complexes
        6.rankings
        7.venues
category & competitions: Provides a list of all available tennis competitions for a given category (ex. ATP, ITF, or WTA).
complexes & venues: Lists all complexes and venues available in the API.
competitor_rankings,competitors & rankings: Provides the top 500 doubles competitor rankings for the ATP and WTA.

query execution for table category & competitions;
  1) List all competitions along with their category name
  2) Count the number of competitions in each category
  3) Find all competitions of type 'doubles'
  4) Get competitions that belong to a specific category (e.g., ITF Men)
  5) Identify parent competitions and their sub-competitions
  6) Analyze the distribution of competition types by category
  7) List all competitions with no parent (top-level competitions)

query execution for table complexes & venues;
  1) List all venues along with their associated complex name
  2) Count the number of venues in each complex
  3) Get details of venues in a specific country (e.g., Chile)
  4) Identify all venues and their timezones
  5) Find complexes that have more than one venue
  6) List venues grouped by country
  7) Find all venues for a specific complex (e.g., Nacional)

query execution for table competitor_rankings,competitors & rankings;
  1) Get all competitors with their rank and points.
  2) Find competitors ranked in the top 5
  3) List competitors with no rank movement (stable rank)
  4) Get the total points of competitors from a specific country (e.g., Croatia)
  5) Count the number of competitors per country
  6) Find competitors with the highest points in the current week

        after execution of queries for all the tables and web application is developed using streamlit library to visulaize the data 

