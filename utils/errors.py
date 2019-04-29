class OrderFailError:

    @property
    def err_text(self, err):
        return f'Order create failed with following error:\n{err}'
