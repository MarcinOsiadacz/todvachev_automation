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

    class Password:
        @staticmethod
        def four_characters():
            return 'asdf'
