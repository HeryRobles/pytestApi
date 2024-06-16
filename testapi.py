import requests

def get_product_details(codigo):
    
    url = f'http://localhost/apis/productos.php?codigo={codigo}'
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        
        if data['status'] == 200:
            return {
                "nombre_producto": data['nombre_producto'],
                "precio": data['precio']
            }
        elif data['status'] == 300:
            return {"error": "Producto no encontrado"}
        else:
            return {"error": "Error en la solicitud. Verifique el código del producto."}
    
    except requests.exceptions.RequestException as e:
        return {"error": f"Error al conectar con la API: {e}"}

if __name__ == "__main__":
    codigo = input('Ingrese el código del producto: ')
    producto = get_product_details(codigo)
    print(producto)
