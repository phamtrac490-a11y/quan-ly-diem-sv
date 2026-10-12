
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dữ liệu và tính toán
data = {
    'Ho_va_ten': ['An', 'Bình', 'Chi', 'Dũng', 'Hà', 'Lan', 'Minh', 'Nam', 'Phúc', 'Trang'],
    'Chuyen_can': [8.0, 8.5, 7.0, 9.0, 7.5, 6.0, 8.5, 7.0, 7.5, 9.0],
    'Giua_ky': [7.5, 8.0, 6.5, 8.5, 7.0, 6.0, 8.0, 7.0, 7.5, 9.0],
    'Cuoi_ky': [8.0, 8.5, 7.0, 9.5, 7.5, 6.0, 9.0, 7.0, 7.5, 9.0]
}
df = pd.DataFrame(data)
df['Tong_ket'] = (0.2 * df['Chuyen_can'] + 0.3 * df['Giua_ky'] + 0.5 * df['Cuoi_ky']).round(2)

def xep_loai(dtk):
    if dtk >= 8.5: return 'Giỏi'
    elif dtk >= 7.0: return 'Khá'
    elif dtk >= 5.0: return 'Trung bình'
    else: return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

# Giao diện Web
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

st.subheader("1. Bảng điểm chi tiết của sinh viên")
st.dataframe(df)

st.subheader("2. Thống kê chung của lớp")
st.write(f"- Điểm tổng kết trung bình: **{df['Tong_ket'].mean():.2f}**")
sv_max = df.loc[df['Tong_ket'].idxmax()]
sv_min = df.loc[df['Tong_ket'].idxmin()]
st.write(f"- Sinh viên cao điểm nhất: **{sv_max['Ho_va_ten']}** ({sv_max['Tong_ket']})")
st.write(f"- Sinh viên thấp điểm nhất: **{sv_min['Ho_va_ten']}** ({sv_min['Tong_ket']})")
st.write(f"- Số sinh viên đạt (>= 5): **{(df['Tong_ket'] >= 5.0).sum()}**")

st.subheader("3. Tra cứu thông tin sinh viên")
selected_student = st.selectbox("Chọn tên sinh viên:", df['Ho_va_ten'])
s_info = df[df['Ho_va_ten'] == selected_student].iloc[0]
st.write(f"Điểm chuyên cần: {s_info['Chuyen_can']} | Giữa kỳ: {s_info['Giua_ky']} | Cuối kỳ: {s_info['Cuoi_ky']}")
st.write(f"Điểm tổng kết: **{s_info['Tong_ket']}** — Xếp loại: **{s_info['Xep_loai']}**")

st.subheader("4. Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(df['Ho_va_ten'], df['Tong_ket'], color='skyblue')
ax.set_xlabel('Họ tên')
ax.set_ylabel('Điểm tổng kết')
ax.set_ylim(0, 10)
st.pyplot(fig)

st.markdown("---")
st.markdown("<p style='text-align: center; font-size: small;'>Người tạo: Nguyễn Cảnh Chương</p>", unsafe_allow_html=True)
