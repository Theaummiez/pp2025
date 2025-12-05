class Courses:
    def __init__(self, data):
        self.id = int(data[0])
        self.name = data[1]
        self.credit = 2  # default

    def __str__(self):
        return (
            f"Id = {self.id}\n"
            f"Name = {self.name}\n"
            f"Credits = {self.credit}\n"
        )

    @staticmethod
    def create_tab(n, input_func):
        return {
            int((info := input_func("Enter course info (Id Name): ").split())[0]):
            Courses(info)
            for _ in range(n)
        }
