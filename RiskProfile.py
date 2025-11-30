# risk_profile_app.py
import streamlit as st

# --- Configuration ---
st.set_page_config(page_title="Risk Profile Questioner", page_icon="📊", layout="centered")

# --- Helper Functions ---
def get_risk_category(score):
    """Determine risk category based on score."""
    if 19 <= score <= 32:
        return "Sangat Konservatif"
    elif 33 <= score <= 45:
        return "Konservatif"
    elif 46 <= score <= 60:
        return "Moderat"
    elif 61 <= score <= 80:
        return "Agresif"
    else:
        return "Skor Tidak Valid" # Should not happen with valid inputs

def get_allocation_recommendation(category):
    """Get allocation recommendation based on risk category."""
    recommendations = {
        "Sangat Konservatif": [
            "• 60% Deposito/Tabungan/Logam Mulia",
            "• 30% Sukuk Tabungan/ORI",
            "• 10% Reksa dana pasar uang"
        ],
        "Konservatif": [
            "• 40% Sukuk/ORI (kupon tetap)",
            "• 30% Deposito/Logam Mulia",
            "• 20% Reksa dana campuran",
            "• 10% Franchise mikro modal ≤Rp50 juta"
        ],
        "Moderat": [
            "• 30% Saham blue-chip / reksa dana campuran",
            "• 25% Sukuk/ORI",
            "• 20% Franchise/usaha skala menengah (Rp50–200 juta)",
            "• 15% Emas",
            "• 10% Kripto ≤5%"
        ],
        "Agresif": [
            "• 45–50% Saham / reksa dana saham",
            "• 15% Pasar obligasi sekunder (ORI/Sukuk)",
            "• 15% Franchise/usaha baru modal >Rp200 juta",
            "• 10% Properti/Reksa dana properti",
            "• 10% Kripto/Trading Emas (risiko tinggi)"
        ]
    }
    return recommendations.get(category, [])

# --- Main App ---
def main():
    # --- Title and Instructions ---
    st.title("RISK PROFILE QUESTIONER")
    st.markdown("**(HumanisGroup - CTAP Series Tools)**")
    st.markdown("""
    **📋 PETUNJUK PENGISIAN:**
    * Tidak ada jawaban “benar” atau “salah”, "baik" atau "buruk".
    * Pilihlah **SATU** jawaban yang paling menggambarkan diri Anda.
    * Jawablah dengan **JUJUR sebagaimana ADANYA** agar hasil dan rekomendasi sesuai kebutuhan Anda.
    * Isilah dengan **lengkap 20 pertanyaan** yang ada.
    * KAMI TIDAK MENYIMPAN JAWABAN ANDA, **Silahkan Screen-Shot SKOR dan REKOMENDASI**
    """)

    # --- Questions and Options ---
    questions = [
        "Saham yang baru Anda beli turun 10%. Apa reaksi Anda?",
        "Seorang teman Anda mendapatkan keuntungan besar dari investasi aset kripto. Apa yang sekiranya akan Anda lakukan?",
        "Seberapa sering Anda mengubah atau mengganti pilihan instrumen investasi Anda, dalam setahun terakhir?",
        "Bagaimana reaksi Anda saat kondisi pasar investasi sedang anjlok secara signifikan?",
        "Berapa target keuntungan (return) dari investasi yang Anda harapkan dalam setahun?",
        "Berapakah besar persentase kerugian maksimum dari total portofolio investasi yang masih bisa Anda toleransi?",
        "Berapa lama jangka waktu Anda berencana untuk tidak menarik atau menggunakan dana yang diinvestasikan ini?",
        "Manakah yang paling menggambarkan pengalaman Anda dalam berinvestasi?",
        "Bagaimana kondisi dana darurat Anda saat ini (idealnya minimal setara 3 bulan pengeluaran)?",
        "Berapa rasio total cicilan utang bulanan Anda dibandingkan dengan penghasilan bulanan Anda saat ini?",
        "Jika Anda tiba-tiba berhenti bekerja hari ini, berapa lama tabungan yang Anda miliki dapat mencukupi biaya hidup?",
        "Bagaimana sifat penghasilan utama bulanan Anda?",
        "Apa tujuan utama dari dana yang Anda investasikan saat ini?",
        "Berapa kira-kira  persentase dana yang diinvestasikan ini jika dibandingkan dengan total kekayaan bersih Anda?",
        "Apakah Anda memiliki kemampuan untuk menambah dana investasi secara rutin?",
        "Seandainya pasar sedang buruk saat target waktu investasi tercapai, seberapa fleksibel Anda menunda tujuan tersebut?",
        "Seberapa penting tingkat likuiditas (kemudahan mencairkan uang) dalam investasi Anda?",
        "Seberapa sering Anda mengikuti pendidikan atau seminar formal mengenai keuangan dan investasi?",
        "Bagaimana status kepemilikan asuransi jiwa dan kesehatan Anda?",
        "Jika Anda mendapatkan sejumlah dana ekstra, ke mana Anda akan memprioritaskan untuk menempatkannya?"
    ]

    options = [
        ["A. Menjual seluruhnya", "B. Menjual sebagian", "C. Menahan (tidak menjual)", "D. Membeli lebih banyak (average down)"],
        ["A. Langsung ikut membeli aset kripto yang sama", "B. Ikut membeli dalam jumlah kecil untuk mencoba", "C. Mencari informasi lebih dalam terlebih dahulu mengenai aset kripto tersebut", "D. Tetap berpegang pada rencana investasi yang sudah dimiliki"],
        ["A. Lebih dari 6 kali", "B. 3 hingga 6 kali", "C. 1 hingga 2 kali", "D. Tidak pernah sama sekali"],
        ["A. Sulit tidur dan merasa cemas", "B. Terus-menerus memeriksa pergerakan harga", "C. Sesekali memeriksa harga, namun tetap tenang", "D. Tetap santai dan tidak terlalu khawatir"],
        ["A. Kurang dari atau sama dengan 5 %", "B. Antara 6 % hingga 10 %", "C. Antara 11 % hingga 15 %", "D. Lebih dari 15 %"],
        ["A. Kurang dari atau sama dengan 5 %", "B. Antara 6 % hingga 15 %", "C. Antara 16 % hingga 25 %", "D. Lebih dari 25 %"],
        ["A. Kurang dari 1 tahun", "B. 1 hingga 3 tahun", "C. 3 hingga 7 tahun", "D. Lebih dari 7 tahun"],
        ["A. Belum pernah berinvestasi", "B. Pernah berinvestasi pada produk berisiko rendah seperti deposito", "C. Pernah berinvestasi pada produk berisiko menengah seperti saham atau obligasi", "D. Pernah berinvestasi pada produk berisiko tinggi seperti derivatif atau aset kripto"],
        ["A. Belum memiliki dana darurat", "B. Memiliki dana darurat untuk kurang dari 1 bulan pengeluaran", "C. Memiliki dana darurat untuk 1 hingga 3 bulan pengeluaran", "D. Memiliki dana darurat untuk lebih dari 3 bulan pengeluaran"],
        ["A. Lebih dari 50 %", "B. Antara 30 % hingga 50 %", "C. Antara 10 % hingga 29 %", "D. Kurang dari 10 % atau tidak memiliki utang"],
        ["A. Kurang dari 1 bulan", "B. 1 hingga 3 bulan", "C. 3 hingga 12 bulan", "D. Lebih dari 12 bulan"],
        ["A. Tidak tetap atau tidak menentu", "B. Tetap, namun sering mengalami keterlambatan", "C. Tetap dan selalu diterima tepat waktu", "D. Tetap, diterima tepat waktu, dan sering ada bonus/tambahan"],
        ["A. Untuk dana darurat", "B. Untuk DP rumah dalam 3 tahun ke depan", "C. Untuk biaya kuliah anak dalam 7 tahun ke depan", "D. Untuk dana pensiun dalam 20 tahun ke depan"],
        ["A. Lebih dari 75 %", "B. Antara 50 % hingga 75 %", "C. Antara 25 % hingga 49 %", "D. Kurang dari 25 %"],
        ["A. Tidak bisa", "B. Terkadang bisa, jika ada sisa dana", "C. Bisa, dalam jumlah kecil secara rutin", "D. Bisa, dalam jumlah besar secara rutin"],
        ["A. Sama sekali tidak bisa ditunda", "B. Bisa ditunda kurang dari 1 tahun", "C. Bisa ditunda antara 1 hingga 3 tahun", "D. Bisa ditunda lebih dari 3 tahun"],
        ["A. Sangat penting", "B. Cukup penting", "C. Kurang penting", "D. Tidak penting"],
        ["A. Tidak pernah", "B. Pernah satu kali", "C. Pernah 2 hingga 3 kali", "D. Sering mengikuti"],
        ["A. Tidak memiliki keduanya", "B. Memiliki salah satu saja", "C. Memiliki keduanya dengan perlindungan standar", "D. Memiliki keduanya dengan perlindungan yang lengkap"],
        ["A. Ditabung di rekening bank biasa", "B. Investasi pada Sukuk Ritel (SR) atau Obligasi Negara Ritel (ORI)", "C. Investasi pada saham atau reksa dana saham", "D. Digunakan sebagai modal untuk usaha baru atau waralaba (franchise)"]
    ]

    # --- Store Answers ---
    answers = []
    # Using session state to persist answers across reruns
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False
    if 'scores' not in st.session_state:
        st.session_state.scores = [None] * len(questions)

    # --- Question Form ---
    with st.form("risk_profile_form"):
        for i, (q, opts) in enumerate(zip(questions, options)):
            st.subheader(f"{i+1}. {q}")
            # Use session state to remember selected answers
            user_answer = st.radio(
                "Pilih jawaban:",
                options=opts,
                key=f"question_{i}",
                index=0 if st.session_state.scores[i] is None else st.session_state.scores[i] - 1 # Pre-select if available
            )
            # Store the numerical score (1 for A, 2 for B, etc.)
            if user_answer:
                # Extract score from option text (A=1, B=2, C=3, D=4)
                score_map = {"A": 1, "B": 2, "C": 3, "D": 4}
                selected_letter = user_answer.split(".")[0] # Get 'A', 'B', 'C', or 'D'
                st.session_state.scores[i] = score_map.get(selected_letter, 1) # Default to 1 if not found

        submitted = st.form_submit_button("Hitung Profil Risiko")

        if submitted:
            # Check if all questions are answered
            if None in st.session_state.scores:
                 st.error("Harap jawab semua pertanyaan sebelum menghitung.")
            else:
                 st.session_state.submitted = True

    # --- Results Display ---
    if st.session_state.submitted and None not in st.session_state.scores:
        total_score = sum(st.session_state.scores)
        risk_category = get_risk_category(total_score)

        st.success("Profil Risiko Anda telah dihitung!")
        st.subheader(f"Total Skor: {total_score}")
        st.subheader(f"Kategori Klasifikasi Risiko: {risk_category}")

        st.subheader("Contoh Alokasi Praktis:")
        allocation_list = get_allocation_recommendation(risk_category)
        if allocation_list:
            for item in allocation_list:
                st.markdown(item)
        else:
             st.write("Rekomendasi alokasi tidak tersedia untuk kategori ini.")
        st.info("""
        **DISCLAIMER:** Responden berusia ≥55 tahun yang masuk Moderat atau Agresif wajib dikonfirmasi ulang oleh penasihat keuangan untuk memastikan:
        - Tujuan investasi ≥7 tahun,
        - Dana darurat ≥6 bulan,
        - Tidak ada utang konsumtif tinggi.
        """)
        # Additional disclaimer in red
        st.markdown("")
        st.markdown(
            "<span style='color:red; font-weight:bold;'>INVESTASI adalah KEGIATAN BERISIKO !!!, tanggung jawab atas keputusan berinvestasi sepenuhnya adalah TANGGUNG JAWAB PRIBADI, baik berdasarkan tools ini maupun tidak. Inventory Risk Profile TIDAK MENJAMIN HASIL INVESTASI.</span>",
            unsafe_allow_html=True
        )

# Run the app
if __name__ == "__main__":
    main()

# Sembunyikan tombol Fork & GitHub di Streamlit Cloud
st.markdown(
    """
    <style>
        /* Sembunyikan tombol Fork dan ikon GitHub */
        .stApp [data-testid="stHeader"] {
            display: none !important;
        }
        /* Jika ingin sembunyikan juga menu 3 titik (More options) */
        .stApp [data-testid="stToolbar"] {
            display: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)



