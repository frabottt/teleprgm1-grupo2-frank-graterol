#Primera Actividad Almacenamiento en Variables e Impresion
NombreCompleto - "Frank Reinaldo Graterol La Roca"
# llamamos a la funcion print(), y devolvemos una cadena multiple
print("hola grop1 Soy:" ,NombreCompleto)


#dada una lista de personas que fueron a vacunarse

#eliminar las ocurrencias del numero 10

print("listado de personas que han sido vacunadas")

tuple("edades")
vEdades= [2, 7, 58, 7, 45, 26, 10, 8, 56, 57, 97, 19, 11, 53, 3, 99, 62, 78, 29, 9, 37, 42, 56, 86, 28, 86, 95, 26, 49, 67, 21, 815, 67, 10, 58, 512, 24, 92, 89, 67, 53, 10, 9, 83, 1, 44, 10, 77, 98, 73, 57]

for vNUm_Edad in vEdades:
    if vNUm_Edad== 10:
        vEdades.remove(10)

for vNum_Edad in vEdades:
    print("edad", vNum_Edad, "años")

Total= len(vEdades)
print("Total", Total + 1)



