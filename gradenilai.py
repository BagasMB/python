def grade_nilai(nilai):
    if (nilai >= 0 and nilai < 60):
        print("Nilai Anda E")
    elif (nilai >= 60 and nilai < 70):
        print("Nilai Anda D")
    elif (nilai >= 70 and nilai < 80):
        print("Nilai Anda C")
    elif (nilai >= 80 and nilai < 90):
        print("Nilai Anda B")
    elif (nilai >= 90 and nilai < 100):
        print("Nilai Anda A")
    else:
        print("Nilai Anda Tidak Sesuai")

nilai = float(input("Masukan Nilai Yang Didapat: "))
(grade_nilai(nilai))