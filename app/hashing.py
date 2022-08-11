from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")  # шифромание согласно схеме с автоматическим шифрованием


class Hash:

    def bcrypt(password: str):
        return pwd_cxt.hash(password)  # Будем шифровать пароль при его создании

    def verify(hashed_password, plain_password):  # сравниваем простой пароль с захешеным
        return pwd_cxt.verify(plain_password, hashed_password)
