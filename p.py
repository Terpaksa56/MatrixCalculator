import streamlit as st
import pandas as pd
import numpy as np
def gauss_jordan(matrix):
    num_rows, num_cols = matrix.shape
    pivot_row = 0
    
    for col in range(num_cols - 1):
        # Mencari pivot
        pivot_value = matrix[pivot_row, col]
        for row in range(pivot_row + 1, num_rows):
            if matrix[row, col] > pivot_value:
                pivot_row = row
                pivot_value = matrix[row, col]
        # Melakukan pertukaran baris jika pivot row bukan baris saat ini
        if pivot_row != col:
            matrix[[pivot_row, col]] = matrix[[col, pivot_row]]
        
        # Mengubah pivot menjadi 1 dengan membagi baris dengan pivot
        matrix[col] = matrix[col] / matrix[col, col]
        
        # Menghilangkan elemen di kolom pivot dari baris lainnya
        for row in range(num_rows):
            if row != col:
                matrix[row] = matrix[row] - matrix[row, col] * matrix[col]
        
        # Pindah ke baris berikutnya
        pivot_row += 1
    
    return matrix
#cramer rules
def cramer_rule(matrix_A, matrix_b):
    det_A = np.linalg.det(matrix_A)
    n = matrix_A.shape[0]
    results = []
    
    for i in range(n):
        matrix_A_copy = matrix_A.copy()
        matrix_A_copy[:, i] = matrix_b
        det_A_i = np.linalg.det(matrix_A_copy)
        result = det_A_i / det_A
        results.append(result)
    
    return results
#untuk title
st.title(':white[MATRIX CALCULATOR]')


#untuk sidebar
with st.sidebar:
    tipe = st.radio('pilih tipe', ['Single Matrix' , 'Double Matrix', 'Gauss Jordan']) #digunakan untuk memilih

#untuk expander (memilih ukuran)
with st.expander('Pilih Ukuran'):
    with st.form('pilih ukuran'):
        
        if tipe == 'Single Matrix':
            row1= st.number_input('ukuran baris dari matriks ', min_value=2)
            col1= st.number_input('ukuran kolom dari matriks ', min_value=2)
            st.form_submit_button('kirim ukuran matriks')

       
        elif tipe == 'Double Matrix':
            row1= st.number_input('ukuran baris dari matriks pertama', min_value=2)
            col1= st.number_input('ukuran kolom dari matriks pertama', min_value=2)
            row2= st.number_input('ukuran baris dari matriks kedua', min_value=2)
            col2= st.number_input('ukuran kolom dari matriks kedua', min_value=2)
            st.form_submit_button('kirim ukuran matriks')

        elif tipe == 'Gauss Jordan':
            row1= st.number_input('ukuran baris dari matriks ', min_value=2)
            col1= st.number_input('ukuran kolom dari matriks ', min_value=2)
            st.form_submit_button('kirim ukuran matriks')


# untuk single matriks
if tipe == 'Single Matrix':
        st.write('data untuk matriks')
        with st.form('Submit Matrix'):
            df_1 = pd.DataFrame(columns=[f'x{index}' for index in range(1, col1 + 1)], index=[f'x{index}' for index in range(1, row1 + 1)], dtype=float)
            df_1_input = st.data_editor(df_1, use_container_width=True, key=1)
            matrix1 = df_1_input.fillna(0).to_numpy()
            oprasi = st.radio('Pilih Oprasi',['Det(A)','A(INVERSE)', 'A(TRANSPOSE)','RANK'])
            if st.form_submit_button('Calculate'):
                if oprasi == 'A(INVERSE)':    
                    if np.isnan(df_1_input.astype(float).values).any():
                        st.warning("Mohon isi angka terlebih dahulu.")
                    elif matrix1.shape[0] != matrix1.shape[1]:
                            st.warning("Ordo matriks harus sama jika mau menghitung inverse.")
                    else:
                        determinan = np.linalg.det(matrix1)
                        if determinan == 0:
                            st.warning("Matriks tersebut adalah matriks singular, jadi tidak bisa dihitung inverse nya. Silahkan coba lagi!")
                        else:
                            inverse = np.linalg.inv(matrix1)
                            bulat_inverse = round(inverse,3)
                            st.write('Hasil inverse nya adalah :',bulat_inverse)
                elif oprasi == 'Det(A)':
                    if np.isnan(df_1_input.astype(float).values).any():
                        st.warning("Mohon isi angka terlebih dahulu.")   
                    elif matrix1.shape[0] != matrix1.shape[1]:
                        st.warning("Ordo matriks harus sama jika mau menghitung determinan.")
                    else:
                        determinan = np.linalg.det(matrix1)
                        bulat_determinan = round(determinan,3)
                        st.write('Hasil determinan nya adalah :', bulat_determinan)
                elif oprasi == 'A(TRANSPOSE)':
                    if np.isnan(df_1_input.astype(float).values).any():
                        st.warning("Mohon isi angka terlebih dahulu.")
                    else:
                        determinan = np.linalg.det(matrix1)
                        if determinan == 0:
                                st.warning("Masukkan angka yang benar!!")
                        else:
                            transpose = np.transpose(matrix1)
                            st.write('Hasil transpose nya adalah :',transpose)
                elif oprasi == ('RANK') :
                    if np.isnan(df_1_input.astype(float).values).any():
                        st.warning("Mohon isi angka terlebih dahulu.")
                    else:
                        rank = np.linalg.matrix_rank(matrix1)
                        st.write('RANK nya adalah :',rank)
                
  
                    
                

                
# untuk double matriks
elif tipe == 'Double Matrix':
        st.write('data untuk matriks')
        with st.form('Submit Matrix'):
            df_1 = pd.DataFrame(columns=[f'x{index}' for index in range(1, col1 + 1)], index=[f'x{index}' for index in range(1, row1 + 1)], dtype=float)
            df_1_input = st.data_editor(df_1, use_container_width=True, key=1)
            df_2= pd.DataFrame(columns=[f'x{index}' for index in range(1,col2+1)], index=[f'x{index}' for index in range(1, row2+1)], dtype=float)
            df_2_input = st.data_editor(df_2, use_container_width=True, key=2)
            matrix1= df_1_input.fillna(0).to_numpy()
            matrix2= df_2_input.fillna(0).to_numpy()
            oprasi = st.radio('Pilih Oprasi',['A*B', 'A+B','A-B'])
            if st.form_submit_button('Calculate'):
                if oprasi == 'A*B':
                    if np.isnan(df_1_input.astype(float).values).any():
                        st.warning("Mohon isi angka terlebih dahulu.")
                    elif matrix1.shape[1] != matrix2.shape[0]:     
                         st.warning("Jumlah kolom matriks pertama harus sama dengan jumlah baris matriks kedua.")
                        # untuk memeriksa apakah jumlah kolom dan baris
                    else :
                        kali = np.matmul(matrix1, matrix2)
                        st.write('Hasil dari perkalian matriks tersebut adalah : ',kali)
                elif oprasi == 'A+B':
                    if np.isnan(df_1_input.astype(float).values).any():
                        st.warning("Mohon isi angka terlebih dahulu.")
                    elif matrix1.shape[0] != matrix1.shape[1]:
                        st.warning("Ordo matriks harus sama jika mau menghitung penjumlahan matriks.")
                    else:
                        tambah = matrix1 + matrix2
                        st.write('Hasil dari penjumlahan matriks tersebut adalah : ',tambah)
                elif oprasi == 'A-B':
                    if np.isnan(df_1_input.astype(float).values).any():
                        st.warning("Mohon isi angka terlebih dahulu.")
                    elif matrix1.shape[0] != matrix1.shape[1]:
                        st.warning("Ordo matriks harus sama jika mau menghitung pengurangan matriks.")
                    else :
                        kurang = matrix1 - matrix2
                        st.write('Hasil dari pengurangan matriks tersebut adalah : ', kurang)
# untuk Gauss Jordan
elif tipe == 'Gauss Jordan':
        st.write('data untuk matriks')
        with st.form('Submit Matrix'):
            df_1 = pd.DataFrame(columns=[f'x{index}' for index in range(1, col1 + 1)], index=[f'x{index}' for index in range(1, row1 + 1)], dtype=float)
            df_1_input = st.data_editor(df_1, use_container_width=True, key=1)
            matrix1 = df_1_input.fillna(0).to_numpy()
            oprasi = st.radio('Pilih Oprasi',[ 'Gauss Jordan'])
            if st.form_submit_button('Calculate'):
                if oprasi == ('Gauss Jordan') :
                    if np.isnan(df_1_input.astype(float).values).any():
                        st.warning("Mohon isi angka terlebih dahulu.")
                    else:
                        gaus =  gauss_jordan(matrix1)
                        st.write('Hasil dari matriks Gauss Jordan tersebut adalah :',gaus)
                        result = gauss_jordan(matrix1)
                        num_rows, num_cols = result.shape
                        solution = result[:, num_cols-1]
                        print("Solusi:")
                        for i, value in enumerate(solution):
                            print(f"x{i+1} = {value}")