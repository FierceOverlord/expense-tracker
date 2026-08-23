def print_format(func):
    def wrapper(self, *args, **kwargs):

        expenses = func(self, *args, **kwargs)


        if not expenses:
            print("No expense found.")
            return

        rows =[
            [str(i), e.title, str(e.amount), e.category, e.date] 
                for i, e in enumerate(expenses, start=1)
        ]

        headers = ["No.", "Title", "Amount", "Category", "Date"]

        width = [
            max(len(headers[i]), max(len(row[i]) for row in rows))
            for i in range(len(headers))
        ]

        print(
            "  ".join(
                f"{headers[i]:<{width[i]}}"
                for i in range(len(headers))
            )
        )

        for row in rows:
            print(
                "  ".join(
                    f"{row[i]:<{width[i]}}"
                    for i in range(len(row))
                )
            )

    return wrapper