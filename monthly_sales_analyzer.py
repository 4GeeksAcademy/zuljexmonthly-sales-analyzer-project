# Example data
sales_data = [
    {"day": 1, "product_a": 202, "product_b": 142, "product_c": 164},
    {"day": 2, "product_a": 206, "product_b": 121, "product_c": 338},
    {"day": 3, "product_a": 120, "product_b": 152, "product_c": 271},
    {"day": 4, "product_a": 174, "product_b": 137, "product_c": 266},
    {"day": 5, "product_a": 199, "product_b": 153, "product_c": 301},
    {"day": 6, "product_a": 230, "product_b": 199, "product_c": 202},
    {"day": 7, "product_a": 101, "product_b": 137, "product_c": 307},
    {"day": 8, "product_a": 137, "product_b": 179, "product_c": 341},
    {"day": 9, "product_a": 287, "product_b": 70, "product_c": 310},
    {"day": 10, "product_a": 157, "product_b": 71, "product_c": 238},
    {"day": 11, "product_a": 148, "product_b": 108, "product_c": 319},
    {"day": 12, "product_a": 287, "product_b": 64, "product_c": 339},
    {"day": 13, "product_a": 289, "product_b": 100, "product_c": 257},
    {"day": 14, "product_a": 154, "product_b": 113, "product_c": 280},
    {"day": 15, "product_a": 150, "product_b": 184, "product_c": 170},
    {"day": 16, "product_a": 172, "product_b": 67, "product_c": 281},
    {"day": 17, "product_a": 188, "product_b": 109, "product_c": 163},
    {"day": 18, "product_a": 108, "product_b": 139, "product_c": 202},
    {"day": 19, "product_a": 229, "product_b": 133, "product_c": 241},
    {"day": 20, "product_a": 210, "product_b": 57, "product_c": 324}
]

def total_sales_by_product(data, product_key):
    """Calculates the total sales of a specific product in 30 days."""
    sales_sum = 0
    
    # Loop on days in sales list
    for item in data:

    
        sales_sum += item[product_key]
    return sales_sum



def average_daily_sales(data, product_key):
    """Calculates the average daily sales of a specific product."""
    total = 0
    count = 0

    for day in data:
        if product_key in day:
            total += day[product_key]
            count += 1
    

    return total / count




def best_selling_day(data):
    """Finds the day with the highest total sales."""
    best_day = None
    highest_total = -1

    for day in data:
        day_total = 0
        for key, value in day.items():
            if key.startswith("product_"):
                day_total += value
        if day_total > highest_total:
            highest_total = day_total
            best_day = day
    return best_day
    


def days_above_threshold(data, product_key, threshold):
    """Counts how many days the sales of a product exceeded a given threshold."""
    count = 0
    threshold = 300

    for day in sales_data:
        value = day[product_key]
        if value > threshold:
            count += 1

    return count


def top_product(data):
    """Determines which product had the highest total sales in 30 days."""
    totals= {}
    for day in data:
        for key, value in day.items():
            if key.startswith("product_"):
                if key in totals:
                    totals[key] += value
                else:
                    totals[key] = value
    best_product = max(totals, key = totals.get)
    return best_product



# Function tests
print("Total sales of product_a:", total_sales_by_product(sales_data, "product_a"))
print("Average daily sales of product_b:", average_daily_sales(sales_data, "product_b"))
print("Day with highest total sales:", best_selling_day(sales_data))
print("Days when product_c exceeded 300 sales:", days_above_threshold(sales_data, "product_c", 300))
print("Product with highest total sales:", top_product(sales_data))
