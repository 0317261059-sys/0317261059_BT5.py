
tuoi = 25
so_du = 0.0
tien_gui = 60000000.0
lai_suat = 0.10
tang_tien_gui = 0.08
muc_tieu = 10000000000.0

nam = 1

print(
    f"{'Năm':<6}"
    f"{'Tuổi':<8}"
    f"{'Số tiền gửi mới (VNĐ)':>25}"
    f"{'Tiền lãi trong năm (VNĐ)':>28}"
    f"{'Tổng tài sản cuối năm (VNĐ)':>32}"
)
print("-" * 99)

while so_du < muc_tieu:
    # Lưu số dư đầu kỳ
    so_du_dau_ky = so_du

    # Tính tiền lãi trong năm
    tien_lai = so_du_dau_ky * lai_suat

    # Cập nhật tổng tài sản cuối năm
    so_du = so_du_dau_ky + tien_lai + tien_gui

    # In báo cáo
    print(
        f"{nam:<6}"
        f"{tuoi:<8}"
        f"{tien_gui:>25,.0f}"
        f"{tien_lai:>28,.0f}"
        f"{so_du:>32,.0f}"
    )

    # Tăng tiền gửi cho năm tiếp theo
    tien_gui = tien_gui * (1 + tang_tien_gui)

    # Chuyển sang năm và tuổi tiếp theo
    nam += 1
    tuoi += 1

print("-" * 99)
print(f"Thời gian tích lũy: {nam - 1} năm")
print(f"Tuổi đạt mục tiêu: {tuoi - 1} tuổi")
print(f"Tổng tài sản đạt được: {so_du:,.0f} VNĐ")
print(f"Vượt mục tiêu: {so_du - muc_tieu:,.0f} VNĐ")
