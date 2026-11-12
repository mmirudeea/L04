def add_exclamation(text):
    """Level 1: Appends an exclamation mark to the text."""
    return text + "!"

def is_positive(number):
    """Level 2: Returns True if the number is strictly greater than 0."""
    return number > 0

def get_last_item(items):
    """Level 3: Returns the last item of a list, or None if empty."""
    if items:
        return items[-1]
    return None

def add_to_list(item, my_list=None):
    """Level 4: Appends an item to a list and returns it."""
    my_list = my_list if my_list else []
    my_list.append(item)
    return my_list

def calculate_discount(price, discount_percent):
    """Level 5: Applies a discount percentage to a price."""
    discount_amount = price * (discount_percent / 100)
    return price - discount_amount