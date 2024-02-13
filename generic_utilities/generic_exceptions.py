
class EcommerceBackendException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class EcommerceBackendSqlException(EcommerceBackendException):
    pass
    