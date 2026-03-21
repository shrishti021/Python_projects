# E-Commerce Discount Engine
# INTERMEDIATE
# 25 pts
# 📌 An online store applies discounts based on order value, membership, and coupon codes. Build the discount calculation logic.
# 🎯 Task: Write a function 
# calculate_discount(price, is_member, coupon_code) that: 
# applies 10% for members, 
# applies coupon discounts (SAVE20=20%, FIRST50=50% for first order), and stacks them correctly. 
# Cap total discount at 60%.

# TODO: 
    # 1. Start with 0% discount
    # 2. Add 10% if member
    # 3. Add coupon discount if valid
    # 4. Cap total discount at 60%
    # 5. Return (final_price, discount_amount, discount_percent)

def calculate_discount(price, is_member, coupon_code):
    total_discount = 0
    coupon_code = coupon_code.upper()
    if coupon_code == "SAVE20":
        total_discount += 20
    elif coupon_code == "FIRST50":
        total_discount += 50
    elif coupon_code != "":
        return "Invalid coupon code"

    if is_member:
        total_discount += 10
    
    #Cap total discount
    if total_discount > 60:
        total_discount = 60
    
    product_discount = (total_discount/100) * price
    final_price = price - product_discount

    return {
        "original_price": price,
        "total_discount_%": total_discount,
        "final_price": round(final_price, 2)
    }

# Test:
print(calculate_discount(1000, True, "SAVE20"))
#Expected: member 10% + coupon 20% = 30% = ₹300 off → ₹700