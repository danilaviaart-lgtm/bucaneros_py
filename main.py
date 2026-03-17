from utils import *

def playgame():
    # Llamamos a la función de utils que prepara todo de una vez
    p1_tablero, p1_tablero_p2, p2_tablero, p2_tablero_p1 = inicializar_juego()
    # Mensaje de Bienvenida
    print_bienvenida()
    # Pregunta de inicio
    respuesta = input("¿Salimos a navegar? (si/no): ").lower().strip()
    play = True if respuesta == "si" else False
    turno = True
    print_generativo()      

    while play:

        if turno:
            print_turno_jugador()
            mostrar_tableros(p1_tablero,p1_tablero_p2)
            
            coord1 = input("Selecciona una fila (1-10): ")
            coord2 = input("Selecciona una columna (1-10): ")
            
            acertado = disparo(coord1, coord2, p2_tablero, p1_tablero_p2)
            
            if not acertado:
                turno = False
        else:
            print_turno_cpu()
            coord_maquina = generador_coord()
            print_lento(f"La CPU dispara a la casilla: {coord_maquina}")
            
            acertado_maquina = recibir_disparo_cpu(p1_tablero, p2_tablero_p1, coord_maquina)
            
            if not acertado_maquina:
                print_lento("Ha fallado... tenemos una oportunidad...")
                turno = True
            else:
                print_lento("¡Que cabrón! Nos ha dado. Va a volver a disparar.")

        # COMPROBACIÓN DE VICTORIA
        if "O" not in p2_tablero:
            gana_jugador()
            play = False
        elif "O" not in p1_tablero:
            gana_cpu()
            play = False

playgame()