

import redis
from SessionBaseRepository import BaseSessionRepository


class RedisRepository(BaseSessionRepository):
    
    def __init__(self, redis_address, redis_port, db) -> None:
        self.rd = redis.Redis(host=redis_address, port=redis_port, db=db)
    
    def save(self, cliend_id, key, value, ttl=30):
        
        self.rd.hset(name=cliend_id, key=key, value=value, )
        
        return super().save(key, value, ttl)
    
    def clear(self, cliend_id):
        self.rd.delete(cliend_id)