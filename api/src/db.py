import motor.motor_asyncio as asyncio

client = asyncio.AsyncIOMotorClient("mongodb://mongodb:27017")
database = client.orbital_witness
titles_collection = database.get_collection("titles")
