class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # ✅ Private method to connect to email server
    def __connect(self, smtp_server):
        pass  # logic to connect

    # ✅ Private method to prepare the email body
    def __prepare_body(self):
        return f"""Hello Someone.
We have {self.name} {self.quantity} times.
Regards, JisshapedCoding."""

    # ✅ Private method to send the email
    def __send(self):
        pass  # logic to send email

    # ✅ Public method to send the email (only one exposed to user)
    def send_email(self):
        self.__connect("smtp.server.com")
        body = self.__prepare_body()
        self.__send()
