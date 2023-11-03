from repository.passwordRepository import passwordRepository


class PasswordController:
    def __init__(self):    
        pr = passwordRepository()
        self.map = pr.select()        