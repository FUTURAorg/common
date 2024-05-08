

import redis
from .SessionBaseRepository import BaseSessionRepository


class RedisSessionManager(BaseSessionRepository):
    
    def __init__(self, redis_address, redis_port, db) -> None:
        self.__rd = redis.Redis(host=redis_address, port=redis_port, db=db)
    
    def save(self, cliend_id, key, value, ttl=30):
        
        self.__rd.hset(name=cliend_id, key=key, value=value, )
        
        return super().save(key, value, ttl)
    
    def clear(self, cliend_id):
        self.__rd.delete(cliend_id)