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
        

        categorias = {
            "Ceviches": [
                {"nombre": "Ceviche Clásico", "precio": 16.0, "imagen": "images/ceviche.jpg"},
                {"nombre": "Ceviche Mixto", "precio": 18.0, "imagen": "images/ceviche_mixto.jpg"},
                {"nombre": "Ceviche de Pota", "precio": 14.0, "imagen": "images/ceviche_pota.jpg"}
            ],
            "Arroces": [
                {"nombre": "Arroz con Mariscos", "precio": 18.0, "imagen": "images/arroz_mariscos.jpg"},
                {"nombre": "Arroz de pescado", "precio": 14.0, "imagen": "images/chaufa_de_pescado.jpg"},
                {"nombre": "Chaufa mixto", "precio": 12.0, "imagen": "images/chaufa_mixto.jpg"}
            ],
            "Sopas": [                   
                {"nombre": "Chilcano", "precio": 20.0, "imagen": "images/chilcano.jpg"},
                {"nombre": "Chilcano Especial", "precio": 22.0, "imagen": "images/chilcano_especial.jpg"},
                {"nombre": "Sudado de Chita", "precio": 10.0, "imagen": "images/sudado_chita.jpg"}
            ],
            "Chicharrones": [
                {"nombre": "Chicharrón de Pescado", "precio": 15.0, "imagen": "images/chicharron_pescado.jpg"},
                {"nombre": "Chicharrón Mixto", "precio": 18.0, "imagen": "images/chicharron_mixto.jpg"},
                {"nombre": "Chicharrón de Pota", "precio": 17.0, "imagen": "images/chicharron_pota.jpg"}
            ],
            "Tortillas": [
                {"nombre": "Tortilla de Pescado", "precio": 14.0, "imagen": "images/tortilla_pescado.jpg"},
                {"nombre": "Tortilla de Mixto", "precio": 10.0, "imagen": "images/tortilla_mixto.jpg"},
                {"nombre": "Tortilla de Mariscos", "precio": 12.0, "imagen": "images/tortilla_mariscos.jpg"}
            ],
            "Especialidad de la Casa": [
                {"nombre": "Jalea Mixta", "precio": 25.0, "imagen": "images/jalea_mixta.jpg"},
                {"nombre": "Jalea de Pescado", "precio": 30.0, "imagen": "images/jalea_de_pescado.jpg"},
                {"nombre": "Cojinova Frita", "precio": 28.0, "imagen": "images/cojinova_frita.jpg"}
            ],
            "Fuentes": [
                {"nombre": "Chicharron de Pescado - 4 personas", "precio": 26.0, "imagen": "images/fuente_chicharron_pescado.jpg"},
                {"nombre": "Ceviche - 4 personas", "precio": 24.0, "imagen": "images/fuente_ceviche.jpg"},
                {"nombre": "Chicharron de Pota - 4 personas", "precio": 32.0, "imagen": "images/fuente_chicharron_pota.jpg"}
            ],
            "Bebidas": [
                {"nombre": "Chicha Morada", "precio": 5.0, "imagen": "images/chicha.jpg"},
                {"nombre": "Cerveza Pilsen", "precio": 5.0, "imagen": "images/cerveza.jpg"},
                {"nombre": "Gaseosa Personal 'Coca-Cola'", "precio": 4.0, "imagen": "images/gaseosa_cocacola.jpg"}
            ],
            "Guarniciones": [
                {"nombre": "Arroz Blanco", "precio": 4.0, "imagen": "images/arroz_blanco.jpg"},
                {"nombre": "Yuca Frita", "precio": 4.0, "imagen": "images/yuca.jpg"},
                {"nombre": "Papa Dorada", "precio": 4.0, "imagen": "images/papa.jpg"}
            ]
        } 



        tabs = st.tabs(list(categorias.keys()))

        # Diccionario para almacenar selección y cantidades
        pedido = {}


        # ---------------- Barra de navegación rápida --------------



        for tab, categoria in zip(tabs, categorias.keys()):
            with tab:
                cols = st.columns(3)

                for i, plato in enumerate(categorias[categoria]):
                    with cols[i]:
                        st.image(plato["imagen"], width=150)
                        st.write(f"**{plato['nombre']}**")
                        st.write(f"S/. {plato['precio']}")

                        seleccionar = st.checkbox(
                            "Seleccionar",
                            key=f"{categoria}_{plato['nombre']}"
                        )

                        if seleccionar:
                            cantidad = st.number_input(
                                "Cantidad",
                                min_value=1,
                                value=1,
                                key=f"{categoria}_{plato['nombre']}_cant"
                            )

                            pedido[plato["nombre"]] = {
                                "precio": plato["precio"],
                                "cantidad": cantidad
                            }



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
