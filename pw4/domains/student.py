import numpy as np

class Student:
    """Student with marks & credits"""

    def __init__(self, data):
        self.id = int(data[0])
        self.name = data[1]
        self.dob = data[2]
        self.marks = {}    
        self.credits = {}   

    def __str__(self):
        return (
            f"Id = {self.id}\n"
            f"Name = {self.name}\n"
            f"Date of Birth = {self.dob}\n"
            f"GPA = {self.calculate_gpa():.2f}\n"
        )

    @staticmethod
    def create_tab(n, input_func):
        """Create n students using a passed input function"""
        return {
            (info := input_func("Enter Id Name Date: ").split())[0]:
            Student(info)
            for _ in range(n)
        }

    def calculate_gpa(self):
        """Compute weighted GPA"""
        if not self.marks:
            return 0.0

        weighted_scores = []
        total_credits = []

        for cid, scores in self.marks.items():
            avg = np.mean(scores)  
            credit = self.credits[cid]

            gpa4 = (avg / 20) * 4  
            weighted_scores.append(gpa4 * credit)
            total_credits.append(credit)

        return sum(weighted_scores) / sum(total_credits)
