from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init(): #Fungsi inisialisasi
    glClearColor(0.0,0.0,0.0,1.0) #Membersihkan layar dan memberikan warna
    gluOrtho2D(0,100,0,100) #Set origin dari grid dan ukurannya 100 x 100
    

def Bresenham(x1,y1,x2,y2):
    #Perhitungan yang diperlukan untuk
    #Bresenham Algoritma
    m = 2 * (y2 - y1)
    pk = m - (x2 - x1)
    y=y1 

    #Memulai menggambar menggunakan Bresenham
    glClear(GL_COLOR_BUFFER_BIT) #Menghapus semua yang kita gambar sebelumnya, jika ada
    glColor3f(1.0,0.0,0.0) #Mengatur warna RGB (1,0,0) yang merah
    glPointSize(10.0) #Mengatur titik dengan radius tertentu yang diberikan
    glBegin(GL_POINTS) #Menetapkan mode point

    for x in range(x1,x2+1):
        #Menggambar pixel
        glVertex2f(x,y)
        pk =pk + m
        if (pk>= 0):
            y=y+1
            pk =pk - 2 * (x2 - x1)
    glEnd()
    glFlush()

def main():
    x1 = int(input("Masukkan x1: "))
    y1 = int(input("Masukkan y1: "))
    x2 = int(input("Masukkan x2: "))
    y2 = int(input("Masukkan y2: "))

    glutInit(sys.argv) #Inisialisasi glut
    glutInitDisplayMode(GLUT_RGB) #Inisialisasi tipe display glut
    glutInitWindowSize(500,500) #Inisialisasi ukuran layar glut
    glutInitWindowPosition(0,0) #Inisiasliasi posisi layar glut
    glutCreateWindow("Menggambar garis menggunakan BRESENHAM") #Inisialisasi pembuatan window
    glutDisplayFunc(lambda: Bresenham(x1,y1,x2,y2))
    glutIdleFunc(lambda: Bresenham(x1,y1,x2,y2))
    init()
    glutMainLoop()
    
main()