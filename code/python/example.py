# pip3 install neo4j
# python3 example.py

from neo4j import GraphDatabase, basic_auth

cypher_query = '''
MATCH (m:Movie {title:$movieTitle})<-[:ACTED_IN]-(a:Person) RETURN a.name as actorName
'''

with GraphDatabase.driver(
    "neo4j://localhost:7687",
    auth=("neo4j", "neo4j")
) as driver:
    result = driver.execute_query(
        cypher_query,
        movieTitle="The Matrix",
        database_="movies")
    for record in result.records:
        print(record['actorName'])
