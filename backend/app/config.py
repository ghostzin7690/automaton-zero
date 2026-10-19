from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    app_name:str='Automaton V4'; database_url:str='sqlite:///./automaton.db'
    groq_api_key:str=''; groq_model:str='openai/gpt-oss-20b'
    mode:str='approval'; run_token:str='change-me'
    research_provider:str='rss'; search_api_key:str=''; search_api_url:str=''
    kiwify_api_key:str=''; kiwify_api_base:str='https://public-api.kiwify.com'
    public_base_url:str=''
    model_config=SettingsConfigDict(env_file='.env',extra='ignore')
settings=Settings()
