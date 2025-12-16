import streamlit as st
from capaLogica.lPedido import LPedido
from datetime import datetime
import pandas as pd

class Interfaz:
    def __init__(self):
        self.__lPedido = LPedido()
        self.construirInterfaz()

    def construirInterfaz(self):
        st.title("REALIZAR PEDIDO")

        # ---------------- Menú horizontal ----------------
        st.subheader("Menú de platos")

        platos = [
            {"nombre": "Ceviche", "precio": 16.0, "imagen": "images/ceviche.jpg"},
            {"nombre": "Leche de Tigre", "precio": 15.0, "imagen": "images/lechetigre.jpg"},
            {"nombre": "Chilcano", "precio": 10.0, "imagen": "images/chilcano.jpg"}
        ]


        # Diccionario para almacenar selección y cantidades
        pedido = {}

        # Mostrar platos horizontalmente
        cols = st.columns(len(platos))
        for idx, plato in enumerate(platos):
            with cols[idx]:
                st.image(plato["imagen"], width=150)
                st.write(f"**{plato['nombre']}**")
                st.write(f"S/. {plato['precio']}")
                seleccionar = st.checkbox("Seleccionar", key=plato["nombre"])
                if seleccionar:
                    cantidad = st.number_input("Cantidad", min_value=1, value=1, key=plato["nombre"]+"_cant")
                    pedido[plato["nombre"]] = {"precio": plato["precio"], "cantidad": cantidad}

        st.markdown("---")

        # ---------------- Información del cliente y resumen ----------------
        col1, col2 = st.columns(2)

        dni = None
        ruc = None
        razon_social = None
        representante_legal = None
        direccion = None

        # Columna 1: datos del cliente
        with col1:
            st.subheader("Información del cliente")
            nombre = st.text_input("Nombre")
            apellidos = st.text_input("Apellidos")
            tipo_cliente = st.selectbox("Tipo de persona", ["Seleccionar", "Natural", "Juridico"])

            if tipo_cliente == "Juridico":
                ruc = st.text_input("RUC")
                razon_social = st.text_input("Razón social")
                representante_legal = st.text_input("Representante legal")
            elif tipo_cliente == "Natural":
                dni = st.text_input("DNI")

            correo = st.text_input("Correo")
            celular = st.text_input("Celular")
            tipo_orden = st.selectbox("Tipo de orden", ["Seleccionar", "Delivery", "Recojo"])

            if tipo_orden == 'Delivery':
                direccion = st.text_input("Dirección")


        # Columna 2: detalle del pedido
        with col2:
            st.subheader("Detalle del pedido")
            total = 0
            detalle_pedido_str = ""  # Aquí se concatenará todo

            if pedido:
                for nombre_plato, datos in pedido.items():
                    linea = f"{nombre_plato} x {datos['cantidad']} = S/. {datos['cantidad']*datos['precio']}"
                    st.write(linea)
            
            # Concatenar en el string, separando por comas
                    detalle_pedido_str += linea + "; "
            
                    total += datos['cantidad'] * datos['precio']
        
                st.write(f"**Total: S/. {total}**")
            else:
                st.write("No se ha seleccionado ningún plato.")

        if st.button('Crear pedido', type="primary"):
            fecha_pedido = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            pedido = {
            'nombres' : nombre,
            'apellidos' : apellidos,
            'tipo_cliente' : tipo_cliente, 
            'dni' : dni,
            'ruc' : ruc,
            'razon_social'  : razon_social,
            'representante_legal' : representante_legal, 
            'correo' : correo,
            'celular' : celular,
            'detalle_pedido' : detalle_pedido_str,
            'fecha_pedido':fecha_pedido ,
            'tipo_orden': tipo_orden,
            'direccion':direccion,
            'total': total
        };

            print(pedido)
            resultado = self.__lPedido.insetarPedidos(pedido)
            if resultado:

                st.success("Pedido registrado correctamente!")

            else:
                st.error("Error al registrar pedido")

        st.markdown("---")
        st.subheader("Pedidos registrados")

        pedidos_registrados = self.__lPedido.mostraPedidos()
        print(pedidos_registrados)

        if pedidos_registrados:
            df_pedidos = pd.DataFrame(pedidos_registrados)
            st.dataframe(df_pedidos)  # Tabla interactiva
        else:
            st.write("No hay pedidos registrados aún.")
