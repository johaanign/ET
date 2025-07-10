productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}




stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}



def stock_marca(productos, stock, stock_modelos):
    marca = str(input("ingrese marca: ")).upper()
    while True:
        for marca in productos:
            if marca in productos:
                print ("producto encotrado")
            else:
                print ("producto no existe en lista")
                return
            
            modelo = (input)("Ingrese la el mpodelo de la marca").upper()
            if modelo not in stock:
                print ("este modelo no existe en la lista")
            else:
                modelo in stock
                stock_modelos = {"marca" : marca, "modelo" : modelo} 
                print (f"el modelo {modelo} de la marca {marca} tiene un stock de {stock_marca}")
                
                
                
                
        





def buscar_precio(productos, stock):
    for stock in productos:
        stock = 0
        while True:
            busqueda = float(input("ingrese el precio del producto"))
            if busqueda not in stock:
                print ("este producto no existe en la lista")
                return
            elif busqueda in stock:
                print ("este producto tiene stock")
                
            
def actualizar_precio(stock):
    if 
     
     
stock_modelos = []
marcas= []

def main():
        

        print ("Menu")
        print("1)stock marca")
        print("2)Busqueda por Precio")
        print("3)Actualizar precio")
        print("4)Salir")
        
        while True:
                opc= int(input("ingrese una de las opciones del menu"))
                
                if opc == 1:
                    def stock_marca (productos, stock, stock_modelos):
                        print ("busqueda de stock exitosa")
                        
                elif opc == 2:
                    def buscar_precio(productos, stock):
                        print ("busqueda exitosa")
                elif opc== 3:
                    continue
                elif opc == 4:
                    print ("hasta pronto!!")
if __name__=="__main__":
    main()