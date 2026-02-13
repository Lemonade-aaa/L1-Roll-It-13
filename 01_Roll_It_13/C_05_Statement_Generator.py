def make_statment(statement, decoration):
    """Adds emoji / additional characters to the start and end of headings"""

    ends = decoration * 3
    print(f"{ends} {statement} {ends}")


# Main routine
make_statment("I love python", "🐍")
make_statment("Round Results", "=")