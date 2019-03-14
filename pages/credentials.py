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


class Invalid:
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
