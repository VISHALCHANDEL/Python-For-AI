class OTTSubscription:
    def __init__(self, id, plan, payment):
        self.id = id
        self.plan = plan
        self.pymt = payment

    def display(self):
        print(self.id)
        print(self.plan)
        print(self.pymt)



class PSub(OTTSubscription):
    def __init__(self, id, plan, payment, screens):
        super().__init__(id, plan, payment)
        self.screens = screens


a = PSub(1, 2, 100, 4)
a.display()