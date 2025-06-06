import mysql.connector
import pandas as pd
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def get_data(query, params=None):
    # Establish connection to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",        # Replace with your host
        user="root",    # Replace with your username
        password="Prabhudhas@1",# Replace with your password
        database="tennis_db"    # Replace with your database name
    )
    
    # Execute the query with or without parameters
    if params:
        df = pd.read_sql(query, conn, params=params)
        rows = df.values.tolist()
    else:
        df = pd.read_sql(query, conn)
        rows = df.values.tolist()
    # Close the connection
    conn.close()
    
    return df



st.set_page_config(page_title="Tennis Dashboard", layout="wide")
st.title("🎾 Tennis Data Analysis")
st.sidebar.selectbox("options",["tennis data analysis"])

st.markdown("""
    <style>
    /* Make tab headers larger */
    .stTabs [data-baseweb="tab"] {
        font-size: 18px !important;
        padding: 1rem 2rem !important;
    }

    /* Optional: adjust tab content padding */
    .stTabs .stTabContent {
        padding-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "🔍 Search", "📊 Leaderboard", "👤 Highest points"])
with tab1:
    
    st.subheader("📊 A Streamlit App for Exploring tennis sport data")
    st.subheader("Total Number Competitors")
    query1="""SELECT COUNT(*) AS "Total Number Of Competitors"
            FROM competitors"""
    df1=get_data(query1)
    str_df1=str(df1["Total Number Of Competitors"][0])
    a,b=st.columns(2)
    a.metric("No of Competitors",str_df1)


    query2="""SELECT COUNT(DISTINCT country) AS "Total Number Of Countries"
            FROM competitors"""
    df2=get_data(query2)
    str_df2=str(df2["Total Number Of Countries"][0])
    b.metric("No Of countries",str_df2)

    graph_query="""SELECT country, COUNT(*) AS player_count
                    FROM competitors
                    GROUP BY country
                    ORDER BY player_count DESC
                    LIMIT 20;"""
    graph_df=get_data(graph_query)
    st.line_chart(graph_df,x="country",y="player_count",color=["#FF0000"],width=1)
    st.divider()
    
    st.subheader("Highest point scored")
    query3="""SELECT 
                  c.name,
                  c.country,
                  c.category_name AS category,
                  r.points AS "Highest Point Scored"
                FROM competitors AS c
                JOIN competitor_rankings AS r ON c.competitor_id = r.competitor_id
                ORDER BY r.points DESC
                LIMIT 1;"""
    df3=get_data(query3)
    
    st.table(df3)
with tab2:
    if tab2:
        st.write("Search players here.")
        names="""SELECT name From COMPETITORS;"""
        player_name=get_data(names)
        players=tuple(player_name['name'])
        st.sidebar.title("Filter Options")
        selected_player=st.sidebar.selectbox("search",players)
        clicked_button=st.sidebar.button("search",key="button1")
    
        rank_range=st.sidebar.slider("Rank range",0, 500,25)
        button2=st.sidebar.button("search",key="button2")

        country="""SELECT DISTINCT country From COMPETITORS
                ORDER BY country ASC;;"""
        country_name=get_data(country)
        countries=tuple(country_name["country"])
        country_selected=st.sidebar.selectbox("select country",countries)
        button3=st.sidebar.button("search",key="button3")


        if clicked_button:
            players_query="""SELECT 
                      c.name AS Name,
                      c.country AS Country,
                      c.country_code,
                      r.points AS Points,
                      r.competitions_played AS "No of Competitions Played",
                      r.c_rank AS "Rank",
                      r.movement AS "Movement In Rank"
                FROM competitors AS c
                JOIN competitor_rankings AS r ON c.competitor_id = r.competitor_id
                WHERE c.name = %s
                ORDER BY points DESC;"""
            set1= get_data(players_query, params=(selected_player,))
            st.table(set1)

        elif button2:
            rank_query="""SELECT 
                        	c.name AS Name,
                        	c.country AS Country,
                        	r.points AS Points,
                        	r.competitions_played AS "No of Competitions Played",
                            r.c_rank AS "Rank",
                        	r.movement AS "Movement In Rank"
                        FROM competitors AS c
                        JOIN competitor_rankings AS r ON c.competitor_id = r.competitor_id
                        WHERE r.c_rank  BETWEEN 0 AND %s
                        ORDER BY r.c_rank ASC;"""
            set2= get_data(rank_query, params=(rank_range,))
            st.table(set2)

        elif button3:
            country_query="""SELECT 
                        	c.name AS Name,
                        	c.country AS Country,
                        	r.points AS Points,
                        	r.competitions_played AS "No of Competitions Played",
                        	r.c_rank AS "Rank",
                        	r.movement AS "Movement In Rank"
                        FROM competitors AS c
                        JOIN competitor_rankings AS r ON c.competitor_id = r.competitor_id
                        WHERE c.country=%s
                        ORDER BY r.points DESC;"""
            set3= get_data(country_query, params=(country_selected,))
            st.table(set3)


with tab3:
    st.subheader("Top 10 Competitors")
    query4="""SELECT 
            	c.name AS Name,
            	c.country AS Country,
                c.category_name AS Category,
            	r.points AS Points,
            	r.competitions_played AS "No of Competitions Played",
            	r.c_rank AS "Rank"
            FROM competitors AS c
            JOIN competitor_rankings AS r ON c.competitor_id = r.competitor_id
            WHERE r.c_rank<=10
            ORDER BY r.c_rank ASC;"""
    df4=get_data(query4)
    st.table(df4)
    st.write("top 10")

with tab4:
    st.subheader("Competitors with Highest Point")
    query5="""SELECT 
            	c.name AS Name,
            	c.country AS Country,
            	c.category_name AS Category,
            	cr.points AS Points,
            	cr.competitions_played AS "No of Competitions Played",
            	r.gender
            FROM 
            	competitor_rankings cr
            JOIN 
            	competitors c ON cr.competitor_id = c.competitor_id
            JOIN 
            	rankings r ON c.category_name = r.name
            WHERE cr.c_rank<=10
            ORDER BY cr.points DESC;"""
    df5=get_data(query5)
    st.table(df5)
    st.write("Highest Point")
