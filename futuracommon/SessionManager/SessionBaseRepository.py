import abc

class BaseSessionRepository(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def save(self, cliend_id, key, value, ttl=30):
        pass
    
    @abc.abstractmethod
    def clear(self, ):
        pass
    
    @abc.abstractmethod
    def get_all(self, client_id):
        pass