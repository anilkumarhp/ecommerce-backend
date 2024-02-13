
class EcommerceBackendException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


# write EcommerceBackendSqlException exception inheriting EcommerceBackendException
class EcommerceBackendSqlException(EcommerceBackendException):
    pass
    