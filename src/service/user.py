from datetime import datetime, timedelta
import bcrypt
from jose import jwt

class UserService:
    encoding: str = "UTF-8"
    secret_key: str = '55ff6ee67c160db15ef0fe8a569fab137d305e2b87f7f6720dbb571f51d0561a'
    jwt_algorithm: str = "HS256"

    def hash_password(self, plain_password: str) -> str:
        hashed_password: bytes = bcrypt.hashpw(plain_password.encode(self.encoding), salt=bcrypt.gensalt())
        return hashed_password.decode(self.encoding)
    
    def verify_password(
        self, plain_password: str, hahsed_password: str
    ) -> bool :
        return bcrypt.checkpw(
            plain_password.encode(self.encoding), 
            hahsed_password.encode(self.encoding)
        )
    
    def create_jwt(self, username: str) -> str:
        return jwt.encode(
            {
                "sub" : username, # unique id
                "exp" : datetime.now() + timedelta(days=1),
            }, 
            self.secret_key, 
            algorithm=self.jwt_algorithm
        )