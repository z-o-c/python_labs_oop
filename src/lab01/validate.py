def validate_name(value):
    if not isinstance(value, str):
        raise ValueError("name должен быть str")
    if not value.strip():
        raise ValueError("name не может быть пустой строкой")

def validate_price(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Price должен быть int или float")
    if not (0 < value <= 99999):
        raise ValueError("Price должен быть от 1 до 99999 (включительно)")
        
def validate_discount(value):
    if not isinstance(value, int):
        raise ValueError("discount должен быть int")    
    if not (0 <= value < 100):
        raise ValueError("discount должен быть от 0 до 99 (включительно)")
        
def validate_stock(value):
    if not isinstance(value, int):
        raise ValueError("Stock должен быть int")    
    if not (0 <= value):
        raise ValueError("Stock должен быть >= 0")
    
def validate_category(value):
    if not isinstance(value, str):
        raise ValueError("category должен быть str")    
    if not value.strip():
        raise ValueError("category не может быть пустой строкой")
    
def validate_product_id(value):
    if not isinstance(value, str):
        raise ValueError("product_id должен быть str")    
    if not value.strip():
        raise ValueError("product_id не может быть пустой строкой")