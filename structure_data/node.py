class Node:
    def __init__(self, data):
        self.data = data #menyumpan data pada node
        self.next = None #self.next digunakan untuk menyimpan alamat node berikutnya dalam linked list
node1 = Node(10) #membuat objek node1 dengan data 10
node2 = Node(20) #membuat objek node2 dengan data 20
node3 = Node(30) #membuat objek node3 dengan data 30
node1.next = node2 #menghubungkan node1 dengan node2
node2.next = node3 #menghubungkan node2 dengan node3
print("Data pada node1:", node1.data) #menampilkan data pada node1
print("Data pada node2:", node1.next.data) #menampilkan data pada node2
print("Data pada node3:", node1.next.next.data) #menampilkan data pada node3
