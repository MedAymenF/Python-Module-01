class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []

    def add(self, account):
        if (not isinstance(account, Account)):
            print('Acoount must be an `Account` object')
        else:
            self.account.append(account)

    @staticmethod
    def is_corrupted(account):
        if (not isinstance(account, Account)):
            return True
        if (len(dir(account)) % 2 == 0):
            return True
        if ('name' not in dir(account)
                or 'id' not in dir(account) or 'value' not in dir(account)):
            return True
        corrupted = True
        for attr in dir(account):
            if attr.startswith('b'):
                return True
            elif attr.startswith('zip') or attr.startswith('addr'):
                corrupted = False
        if corrupted:
            return True
        return False

    def find_account_by_id(self, id):
        for account in self.account:
            if (account.id == id):
                return account
        return None

    def find_account_by_name(self, name):
        for account in self.account:
            if (account.name == name):
                return account
        return None

    def transfer(self, origin, dest, amount):
        """
            @origin: int(id) or str(name) of the first account
            @dest: int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """
        try:
            assert isinstance(origin, (int, str)),\
                'origin: int(id) or str(name)'
            assert isinstance(dest, (int, str)), 'dest: int(id) or str(name)'
            assert isinstance(amount, (float, int)), 'amount: float(amount)'
            assert amount >= 0, "amount can't be negative"
        except Exception as e:
            print(e)
            return False

        if (isinstance(origin, int)):
            origin_acc = self.find_account_by_id(origin)
        elif (isinstance(origin, str)):
            origin_acc = self.find_account_by_name(origin)
        else:
            print('Account can only be int(id) or str(name)')
        if (isinstance(dest, int)):
            dest_acc = self.find_account_by_id(dest)
        elif (isinstance(dest, str)):
            dest_acc = self.find_account_by_name(dest)
        else:
            print('Account can only be int(id) or str(name)')

        if (not origin_acc or not dest_acc):
            print("Account not found")
            return False

        if (self.is_corrupted(origin_acc)):
            print("Origin account corrupted")
            return False
        if (self.is_corrupted(dest_acc)):
            print("Destination account corrupted")
            return False

        if (origin_acc.value < amount):
            print("Funds insufficient")
            return False

        dest_acc.value += amount
        origin_acc.value -= amount
        return True

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) or instance of the account
            @return True if success, False if an error occured
        """
        if (isinstance(account, int)):
            account = self.find_account_by_id(account)
        elif (isinstance(account, str)):
            account = self.find_account_by_name(account)
        elif (not isinstance(account, Account)):
            return False
        if not account:
            print('Account not found')
            return False
        if not hasattr(account, 'name'):
            account.name = ''
        if not hasattr(account, 'id'):
            account.id = Account.ID_COUNT
            Account.ID_COUNT += 1
        if not hasattr(account, 'value'):
            account.value = 0
        no_start = True
        for attr in dir(account):
            if attr.startswith('zip') or attr.startswith('addr'):
                no_start = False
                break
        if no_start:
            account.zip = 0
        for attr in dir(account):
            if attr.startswith('b'):
                delattr(account, attr)
        if (len(dir(account)) % 2 == 0):
            account.useless = 'useless'
        return True
