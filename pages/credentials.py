class Valid:
    @staticmethod
    def username():
        return 'ValidUser'

    @staticmethod
    def password():
        return 'asdf1234!'

    @staticmethod
    def email():
        return 'example@example.com'

    @staticmethod
    def user_id():
        return 'asdf1'

    @staticmethod
    def address():
        return 'Street1'

    @staticmethod
    def zip_code():
        return '12345'

    @staticmethod
    def name():
        return 'Asdf'


class Invalid:
    class ZipCode:
        @staticmethod
        def with_letters():
            return '1234f'

        @staticmethod
        def with_special_symbols():
            return '1$34%'

        @staticmethod
        def with_space():
            return '12 345'

    class Address:
        @staticmethod
        def with_special_symbols():
            return 'asdf1%'

    class Name:
        @staticmethod
        def with_digits():
            return 'asdf1'

    class UserID:
        @staticmethod
        def four_characters():
            return 'asdf'

        @staticmethod
        def thirteen_characters():
            return 'asdfasdfasdf1'

    class Username:
        @staticmethod
        def four_characters():
            return 'asdf'

        @staticmethod
        def thirteen_characters():
            return 'asdfasdfasdf1'

        @staticmethod
        def only_letters():
            return 'asdfasdf'

        @staticmethod
        def only_numbers():
            return '123456789'

        @staticmethod
        def only_special_symbols():
            return '!@#$%^&*('

        @staticmethod
        def no_special_symbols():
            return 'asdf1234'

    class Password:
        @staticmethod
        def four_characters():
            return 'asdf'

        @staticmethod
        def thirteen_characters():
            return 'asdfasdfasdf1'

        @staticmethod
        def only_letters():
            return 'asdfasdf'

        @staticmethod
        def only_numbers():
            return '123456789'

        @staticmethod
        def only_special_symbols():
            return '!@#$%^&*('

        @staticmethod
        def no_special_symbols():
            return 'asdf1234'

    class Email:
        @staticmethod
        def no_user():
            return '@asdf.com'

        @staticmethod
        def not_at():
            return 'asdfasdf.com'

        @staticmethod
        def no_domain():
            return 'asdf@'

        @staticmethod
        def no_extension():
            return 'asdf@asdf'
