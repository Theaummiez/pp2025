import curses

def display_sorted_students(students):
    sorted_list = sorted(
        students.values(),
        key=lambda s: s.calculate_gpa(),
        reverse=True
    )

    def ui(screen):
        screen.clear()
        screen.addstr(0, 0, "=== Students sorted by GPA ===")
        for i, s in enumerate(sorted_list, start=2):
            screen.addstr(i, 0, f"{s.name} | GPA = {s.calculate_gpa():.2f}")
        screen.refresh()
        screen.getch()

    curses.wrapper(ui)
