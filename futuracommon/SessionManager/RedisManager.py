

import redis
from .SessionBaseRepository import BaseSessionRepository


class RedisSessionManager(BaseSessionRepository):
    
    def __init__(self, redis_address, redis_port, db) -> None:
        self.__rd = redis.Redis(host=redis_address, port=redis_port, db=db, decode_responses=True )
    
    def save(self, cliend_id, key, value, ttl=45):
        
        self.__rd.hset(name=cliend_id, key=key, value=value, )
        self.__rd.expire(name=cliend_id, time=ttl, gt=True)
        
        
        return super().save(key, value, ttl)
    
    def clear(self, cliend_id):
        self.__rd.delete(cliend_id)
    
    def get_all(self, client_id):
        return self.__rd.hgetall(client_id)