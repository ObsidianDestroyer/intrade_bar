class OrderFailError(Exception):
    def __init__(self, *err):
        self.err = err

    @property
    def err_text(self, err):
        return f'Order create failed with following error:\n{err}'
