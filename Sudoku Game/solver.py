def solusi(kotak):
    ketemu = kotakkosong(kotak)
    if not ketemu:
        return True
    else:
        baris, kolom = ketemu

    for i in range(1,10):
        if cekvalid(kotak, i, (baris, kolom)):
            kotak[baris][kolom] = i

            if solusi(kotak):
                return True

            kotak[baris][kolom] = 0

    return False


def cekvalid(kotak, angka, posisi):

    # cek baris
    for i in range(len(kotak[0])):
        if kotak[posisi[0]][i] == angka and posisi[1] != i:
            return False

    # cek kolom
    for i in range(len(kotak)):
        if kotak[i][posisi[1]] == angka and posisi[0] != i:
            return False

    # cek kotak area/grid
    kotak_x = posisi[1] // 3
    kotak_y = posisi[0] // 3

    for i in range(kotak_y*3, kotak_y*3 + 3):
        for j in range(kotak_x * 3, kotak_x*3 + 3):
            if kotak[i][j] == angka and (i,j) != posisi:
                return False

    return True


def print_papan(kotak):
    for i in range(len(kotak)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -  ")

        for j in range(len(kotak[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(kotak[i][j])
            else:
                print(str(kotak[i][j]) + " ", end="")


def kotakkosong(kotak):
    for i in range(len(kotak)):
        for j in range(len(kotak[0])):
            if kotak[i][j] == 0:
                return (i, j)

    return None
