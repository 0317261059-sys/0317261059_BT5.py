
# Khởi tạo thông số trái phiếu
F = 1000000.0       # Mệnh giá trái phiếu
c = 0.09            # Lãi suất coupon 9%
N = 10              # Thời hạn 10 năm
y = 0.085           # Lợi suất thị trường 8.5%

# 1. Tính tiền lãi coupon hằng năm
C = F * c

print(f"Tiền lãi coupon hàng năm: {C:,.0f} VNĐ")
print("-" * 75)

# 2. Tính giá trị hiện tại của từng khoản coupon
tong_pv_coupon = 0.0

print(f"{'Năm':<10}{'Coupon (VNĐ)':>20}{'PV Coupon (VNĐ)':>25}")
print("-" * 55)

for t in range(1, N + 1):
    pv_c = C / ((1 + y) ** t)
    tong_pv_coupon += pv_c

    print(f"{t:<10}{C:>20,.0f}{pv_c:>25,.2f}")

# 3. Tính giá trị hiện tại của mệnh giá gốc
pv_f = F / ((1 + y) ** N)

# 4. Tính giá lý thuyết trái phiếu
gia_trai_phieu = tong_pv_coupon + pv_f

print("-" * 75)
print(f"Tổng PV coupon:       {tong_pv_coupon:,.2f} VNĐ")
print(f"PV mệnh giá gốc:      {pv_f:,.2f} VNĐ")
print(f"Giá trái phiếu P0:    {gia_trai_phieu:,.2f} VNĐ")

# 5. Phân loại trái phiếu
if gia_trai_phieu > F:
    print("Phân loại: Premium (Cao hơn mệnh giá)")
elif gia_trai_phieu < F:
    print("Phân loại: Discount (Thấp hơn mệnh giá)")
else:
    print("Phân loại: Par (Đúng mệnh giá)")
