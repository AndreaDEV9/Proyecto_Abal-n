import os 
from dotenv import load_dotenv
from supabase import create_client


class ConexionDB:
    def __init__(self):
        load_dotenv()

    def conexionSupaBase(self):
        url = os.getenv('SUPABASE_URL')
        api_key = os.getenv('SUPABASE_APIKEY')

        supabase = create_client(url,api_key)
        return supabase
    
"""
objetoPrueba = ConexionDB()
print(objetoPrueba.conexionSupaBase())
"""