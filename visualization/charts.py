import matplotlib.pyplot as plt  # pyright: ignore[reportMissingModuleSource]

def plot_spending_by_category(category_totals):
    """
    category_totals: dict like {"food": 5000, "transport": 2000, "shopping": 3000}
    """
    if not category_totals:
        print("No data to visualize.")
        return

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure(figsize=(8,5))
    plt.bar(categories, amounts, color="#4C72B0")
    plt.title("Spending By Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.show()

def plot_spending_by_month(monthly_totals):
    """
    monthly_totals: dict like {"2026-07": 5000, "2026-08": 7000, "2026-09": 3000}
    """
    if not monthly_totals:
        print("No data to visualize.")
        return

    months = sorted(monthly_totals.keys())
    amounts = [monthly_totals[m] for m in months]

    plt.figure(figsize=(9, 5))
    plt.plot(months, amounts, marker="o", color="#DD8452")
    plt.title("Spending by Month")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_spending_distribution(category_totals, threshold_pct=5):
    """
    Same data as plot_spending_by_category, different view — pie chart.
    """
    if not category_totals:
        print("No data to visualize.")
        return

    total = sum(category_totals.values())
    grouped = {}
    other = 0

    for category, amount in category_totals.items():
        if (amount/total) * 100 < threshold_pct:
            other += amount
        else:
            grouped[category] = amount

    if other > 0:
        grouped["Other"] = other

    plt.figure(figsize=(6, 6))
    plt.pie(
            grouped.values(), 
            labels=grouped.keys(), 
            autopct="%1.1f%%", 
            startangle=90, 
            pctdistance=0.8,       # pulls percentage text closer to the edge, away from center
            labeldistance=1.1      # pushes category names further outside the pie)
            )     
    plt.title("Spending Distribution")
    plt.tight_layout()
    plt.show()