from sqlalchemy import MetaData, create_engine
from sqlalchemy_schemadisplay import create_schema_graph

from config import DB_PATH

engine = create_engine(DB_PATH)

metadata = MetaData()
metadata.reflect(bind=engine)

graph = create_schema_graph(engine=engine, metadata=metadata)

graph.write_png("database_schema.png")
