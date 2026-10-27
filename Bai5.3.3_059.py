
# Khởi tạo giá trị danh mục và các kịch bản
V_goc = 20.0  # Đơn vị: tỷ VNĐ

kich_ban_ty_gia = [-0.03, 0.00, 0.03]
kich_ban_lai_suat = [-0.02, -0.01, 0.01, 0.02]

print("=== MA TRẬN PHÂN TÍCH ĐỘ NHẠY GIÁ TRỊ DANH MỤC (TỶ VNĐ) ===")
print(f"Vốn danh mục ban đầu: {V_goc:.2f} Tỷ VNĐ\n")

# In tiêu đề các cột
print("Thay đổi Lãi suất (Dòng) \\ Tỷ giá (Cột) |", end=" ")
for delta_Ex in kich_ban_ty_gia:
    print(f"{delta_Ex * 100:+.1f}%".replace("+0.0%", "0.0%").rjust(10), end=" | ")
print()

print("-" * 76)

# Vòng lặp ngoài: duyệt các kịch bản lãi suất
for delta_Ir in kich_ban_lai_suat:
    print(f"Lãi suất: {delta_Ir * 100:+.1f}%".replace("+0.0%", "0.0%").ljust(25), end=" | ")

    # Vòng lặp trong: duyệt các kịch bản tỷ giá
    for delta_Ex in kich_ban_ty_gia:
        V_moi = V_goc * (1 + 1.5 * delta_Ex - 2.0 * delta_Ir)
        print(f"{V_moi:.2f} Tỷ".rjust(10), end=" | ")

    print()  # Xuống dòng sau mỗi kịch bản lãi suất

print("-" * 76)
