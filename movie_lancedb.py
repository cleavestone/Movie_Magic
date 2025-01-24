import lancedb
import pandas as pd

#Load our preprocessed data, 
# refer to the Jupyter notebook for the preprocessing steps
df = pd.read_pickle(r"C:\Users\Hp\Desktop\movie_recommender\data\movies.pkl")

# Define the URI for the LanceDB database
uri = "data/movies_lancedb"
# Connect to the LanceDB database at the specified URI
db = lancedb.connect(uri)

if "movies" in db.table_names():
    db.drop_table("movies")

table1 = db.create_table("movies", df)



