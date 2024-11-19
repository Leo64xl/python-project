import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

class Cliente:
    def __init__(self, id_cliente, nombre):
        self.id_cliente = id_cliente
        self.nombre = nombre

class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

class Venta:
    def __init__(self, cliente):
        self.cliente = cliente
        self.detalles = []  

    def agregar_producto(self, producto, cantidad):
        self.detalles.append((producto, cantidad))

    def calcular_subtotal(self):
        return sum(producto.precio * cantidad for producto, cantidad in self.detalles)

    def calcular_iva(self):
        return self.calcular_subtotal() * 0.16

    def calcular_total(self):
        return self.calcular_subtotal() + self.calcular_iva()

    def generar_ticket(self):
        ticket = f"Cliente: {self.cliente.nombre}\n"
        for producto, cantidad in self.detalles:
            ticket += f"{producto.nombre} (x{cantidad}): ${producto.precio * cantidad:.2f}\n"
        ticket += f"Subtotal: ${self.calcular_subtotal():.2f}\n"
        ticket += f"IVA: ${self.calcular_iva():.2f}\n"
        ticket += f"Total: ${self.calcular_total():.2f}\n"
        return ticket

class SistemaTienda:
    def __init__(self):
        self.clientes = {}
        self.productos = {}
        self.ventas = []

    def agregar_cliente(self, id_cliente, nombre):
        self.clientes[id_cliente] = Cliente(id_cliente, nombre)

    def agregar_producto(self, codigo, nombre, precio):
        self.productos[codigo] = Producto(codigo, nombre, precio)

    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            return True
        return False

    def realizar_venta(self, id_cliente):
        cliente = self.clientes.get(id_cliente)
        if cliente:
            venta = Venta(cliente)
            self.ventas.append(venta)
            return venta
        return None

    def obtener_registros_ventas(self):
        return self.ventas  

sistema = SistemaTienda()
venta_actual = None

contraseñas = {
    "admin": "admin123",
    "usuario": "usuario123"
}

def iniciar_sesion():
    rol = entrada_rol.get().lower()
    password = entrada_password.get()

    if rol in contraseñas and contraseñas[rol] == password:
        if rol == "admin":
            mostrar_frame(frame_admin)
        else:
            mostrar_frame(frame_usuario)
    else:
        messagebox.showerror("Error", "Rol o contraseña no válidos")

def mostrar_frame(frame):
    frame_login.pack_forget()
    frame_admin.pack_forget()
    frame_usuario.pack_forget()
    frame.pack(fill="both", expand=True)

def interfaz_administrador():
    frame_admin.columnconfigure(0, weight=1)
    frame_admin.columnconfigure(1, weight=1)

    ctk.CTkLabel(frame_admin, text="Interfaz Admin", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

    ctk.CTkLabel(frame_admin, text="Código Producto:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entrada_codigo_producto = ctk.CTkEntry(frame_admin, placeholder_text="Código Producto")
    entrada_codigo_producto.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    ctk.CTkLabel(frame_admin, text="Nombre Producto:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entrada_nombre_producto = ctk.CTkEntry(frame_admin, placeholder_text="Nombre Producto")
    entrada_nombre_producto.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    ctk.CTkLabel(frame_admin, text="Precio Producto:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    entrada_precio_producto = ctk.CTkEntry(frame_admin, placeholder_text="Precio Producto")
    entrada_precio_producto.grid(row=3, column=1, padx=10, pady=5, sticky="w")
   
    boton_agregar_producto = ctk.CTkButton(frame_admin, text="Agregar Producto", 
        command=lambda: agregar_producto(entrada_codigo_producto.get(), 
                                          entrada_nombre_producto.get(), 
                                          entrada_precio_producto.get()), width=310)
    boton_agregar_producto.grid(row=4, column=0, columnspan=2, pady=10)

    ctk.CTkLabel(frame_admin, text="Eliminar Producto", font=("Helvetica", 16, "bold")).grid(row=5, column=0, columnspan=2, pady=10)

    ctk.CTkLabel(frame_admin, text="Código Producto a Eliminar:").grid(row=6, column=0, padx=10, pady=5, sticky="e")
    entrada_codigo_eliminar = ctk.CTkEntry(frame_admin, placeholder_text="Código Del Producto")
    entrada_codigo_eliminar.grid(row=6, column=1, padx=10, pady=5, sticky="w")

    boton_eliminar_producto = ctk.CTkButton(frame_admin, text="Eliminar Producto", 
        command=lambda: eliminar_producto(entrada_codigo_eliminar.get()), width=310)
    boton_eliminar_producto.grid(row=7, column=0, columnspan=2, pady=10)

    ctk.CTkLabel(frame_admin, text="Lista de Productos", font=("Helvetica", 16, "bold")).grid(row=8, column=0, columnspan=2, pady=10)
    global lista_productos
    lista_productos = ctk.CTkTextbox(frame_admin, height=10)
    lista_productos.grid(row=9, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

    ctk.CTkLabel(frame_admin, text="Registros de Ventas", font=("Helvetica", 16, "bold")).grid(row=10, column=0, columnspan=2, pady=10)
    global lista_registros_ventas
    lista_registros_ventas = ctk.CTkTextbox(frame_admin, height=10)
    lista_registros_ventas.grid(row=11, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

    boton_mostrar_productos = ctk.CTkButton(frame_admin, text="Mostrar Productos Disponibles", 
        command=mostrar_productos, width=310)
    boton_mostrar_productos.grid(row=12, column=0, columnspan=2, pady=10)

    boton_mostrar_registros = ctk.CTkButton(frame_admin, text="Mostrar Registros de Ventas", 
        command=mostrar_registros_ventas, width=310)
    boton_mostrar_registros.grid(row=13, column=0, columnspan=2, pady=10) 

    boton_volver = ctk.CTkButton(frame_admin, text="Cerrar Sesion", command=lambda: mostrar_frame(frame_login), width=310)
    boton_volver.grid(row=14, column=0, columnspan=2, pady=10)

def agregar_producto(codigo, nombre, precio):
    try:
        precio = float(precio)
        if codigo and nombre and precio >= 0:
            sistema.agregar_producto(codigo, nombre, precio)
            messagebox.showinfo("Producto Agregado", f"Producto {nombre} agregado con éxito.")
            mostrar_productos()  
        else:
            messagebox.showerror("Error", "Por favor, ingrese datos válidos.")
    except ValueError:
        messagebox.showerror("Error", "El precio debe ser un número válido.")

def eliminar_producto(codigo):
    if sistema.eliminar_producto(codigo):
        messagebox.showinfo("Producto Eliminado", f"Producto con código {codigo} eliminado con éxito.")
        mostrar_productos()
    else:
        messagebox.showerror("Error", "Producto no encontrado.")

def mostrar_productos():
    lista_productos.delete("1.0", tk.END)  
    for producto in sistema.productos.values():
        lista_productos.insert(tk.END, f"Código: {producto.codigo}, Nombre: {producto.nombre}, Precio: ${producto.precio:.2f}\n")

def mostrar_registros_ventas():
    lista_registros_ventas.delete("1.0", tk.END)  
    for venta in sistema.obtener_registros_ventas():
        lista_registros_ventas.insert(tk.END, venta.generar_ticket() + "\n" + "-"*40 + "\n")

def interfaz_usuario():
    frame_usuario.columnconfigure(0, weight=1)
    frame_usuario.columnconfigure(1, weight=1)

    ctk.CTkLabel(frame_usuario, text="Interfaz Usuario", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

    ctk.CTkLabel(frame_usuario, text="ID Producto:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entrada_id_producto = ctk.CTkEntry(frame_usuario, placeholder_text="ID Producto")
    entrada_id_producto.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    ctk.CTkLabel(frame_usuario, text="Nombre Cliente:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entrada_nombre_cliente = ctk.CTkEntry(frame_usuario, placeholder_text="Nombre Cliente")
    entrada_nombre_cliente.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    boton_generar_ticket = ctk.CTkButton(frame_usuario, text="Generar Ticket", command=lambda: generar_ticket(entrada_id_producto.get(), entrada_nombre_cliente.get()), width=250)
    boton_generar_ticket.grid(row=3, column=0, columnspan=2, pady=10)

    ctk.CTkLabel(frame_usuario, text="Lista de Productos", font=("Helvetica", 16, "bold")).grid(row=4, column=0, columnspan=2, pady=10)
    global lista_productos_usuario
    lista_productos_usuario = ctk.CTkTextbox(frame_usuario, height=10)
    lista_productos_usuario.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

    boton_mostrar_productos_usuario = ctk.CTkButton(frame_usuario, text="Mostrar Productos Disponibles", command=mostrar_productos_usuario, width=250)
    boton_mostrar_productos_usuario.grid(row=6, column=0, columnspan=2, pady=10)

    ctk.CTkLabel(frame_usuario, text="Detalles del Ticket", font=("Helvetica", 16, "bold")).grid(row=7, column=0, columnspan=2, pady=10)

    global etiqueta_producto_comprado
    etiqueta_producto_comprado = ctk.CTkLabel(frame_usuario, text="")
    etiqueta_producto_comprado.grid(row=8, column=0, columnspan=2, pady=5)

    global etiqueta_iva
    etiqueta_iva = ctk.CTkLabel(frame_usuario, text="")
    etiqueta_iva.grid(row=9, column=0, columnspan=2, pady=5)

    global etiqueta_total
    etiqueta_total = ctk.CTkLabel(frame_usuario, text="")
    etiqueta_total.grid(row=10, column=0, columnspan=2, pady=5)

    boton_volver = ctk.CTkButton(frame_usuario, text="Cerrar Sesion", command=lambda: mostrar_frame(frame_login), width=210)
    boton_volver.grid(row=11, column=0, columnspan=2, pady=10)

def mostrar_productos_usuario():
    lista_productos_usuario.delete("1.0", tk.END)  
    for producto in sistema.productos.values():
        lista_productos_usuario.insert(tk.END, f"Código: {producto.codigo}, Nombre: {producto.nombre}, Precio: ${producto.precio:.2f}\n")

def generar_ticket(id_producto, nombre_cliente):
    global venta_actual
    cliente_id = nombre_cliente  
    sistema.agregar_cliente(cliente_id, nombre_cliente)  
    venta_actual = sistema.realizar_venta(cliente_id)
    producto = sistema.productos.get(id_producto)

    if venta_actual and producto:
        venta_actual.agregar_producto(producto, 1) 
        ticket = venta_actual.generar_ticket()
        messagebox.showinfo("Ticket", ticket)
        etiqueta_producto_comprado.configure(text=f"Producto Comprado: {producto.nombre}, Precio: ${producto.precio:.2f}")
        etiqueta_iva.configure(text=f"IVA: ${venta_actual.calcular_iva():.2f}")
        etiqueta_total.configure(text=f"Importe Total: ${venta_actual.calcular_total():.2f}")
    else:
        messagebox.showerror("Error", "No se pudo generar el ticket.")

ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("Sistema de Tienda")
ventana.geometry("600x400")

frame_login = ctk.CTkFrame(ventana)
frame_login.pack(fill="both", expand=True)

frame_admin = ctk.CTkFrame(ventana)
frame_usuario = ctk.CTkFrame(ventana)

# Diseño de la interfaz de inicio de sesión
frame_login.columnconfigure(0, weight=1)
frame_login.columnconfigure(1, weight=1)

etiqueta_rol = ctk.CTkLabel(frame_login, text="¡Bienvenido de nuevo!", font=("Helvetica", 18, "bold"))
etiqueta_rol.grid(row=0, column=0, columnspan=2, pady=20)

etiqueta_rol = ctk.CTkLabel(frame_login, text="Rol:")
etiqueta_rol.grid(row=1, column=0, padx=10, pady=10, sticky="e")

entrada_rol = ctk.CTkEntry(frame_login, placeholder_text="admin/usuario")
entrada_rol.grid(row=1, column=1, padx=10, pady=10, sticky="w")

etiqueta_password = ctk.CTkLabel(frame_login, text="Clave:")
etiqueta_password.grid(row=2, column=0, padx=10, pady=10, sticky="e")

entrada_password = ctk.CTkEntry(frame_login, placeholder_text="******", show="*")
entrada_password.grid(row=2, column=1, padx=10, pady=10, sticky="w")

boton_login = ctk.CTkButton(frame_login, corner_radius=6, text="Iniciar Sesión", command=iniciar_sesion, width=200)
boton_login.grid(row=3, column=0, columnspan=2, pady=15)

interfaz_administrador()
interfaz_usuario()

ventana.mainloop()