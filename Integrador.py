Productos = [[1, "Maíz en grano", 285.55], [2, "Pepino", 334.72], [3, "Tomate verde00", 129.00]]

Ventas_productos = [[2,122], 
[1,89], 
[1,22], 
[3,48],
[1,75],
[3,322],
[2,95],
[1,148],
[1,83],
[3,100]]


Cajas_venta = int(input("Digite la cantidad total de cajas paraa vender: "))
ID_producto = int(input('Ingresa el ID del producto: '))


for producto in Productos:
  if producto[0] == ID_producto:
    Ventas_productos.append([ID_producto, Cajas_venta])
    print(f' El producto es: {producto[1]}')
    print(f' El precio por caja es: {producto[2]}')
    total = producto[2] * Cajas_venta
    if Cajas_venta <= 100:
      total += 1500 
    total_de_cajas = 0
    for venta in Ventas_productos:
      total_de_cajas += venta[1]
      
    if total_de_cajas > 1500:
      descuento = total * 0.20
      total = total - descuento

    print(f'Aplica el descuento del 20%: {total_de_cajas > 1500:}')
    print(f'El total a pagar es: {round(total, 2)}')