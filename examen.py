def sistema_reservas():
    reservas = {}
    tipos_habitaciones = set()

    # Almacenamiento de reservas
    for _ in range(int(input("Número de reservas a ingresar: "))):
        num_hab = input("Número de habitación: ")
        tipo_hab = input("Tipo de habitación: ")
        huesped = input("Nombre del huésped: ")
        reservas[(num_hab, tipo_hab)] = huesped
        tipos_habitaciones.add(tipo_hab)

    # Visualización de reservas
    print("Reservas registradas:")
    for (num_hab, tipo_hab), huesped in reservas.items():
        print(f"Habitación {num_hab} ({tipo_hab}): {huesped}")

    # Tipos de habitaciones disponibles
    print("\nTipos de habitaciones disponibles:", tipos_habitaciones)

    # Consultar disponibilidad
    consulta = (input("\nConsultar habitación (número): "), input("Tipo: "))
    print("Ocupada" if consulta in reservas else "Libre")

    # Cancelar reserva
    cancelar = (input("\nCancelar habitación (número): "), input("Tipo: "))
    if cancelar in reservas:
        del reservas[cancelar]
        print("Reserva cancelada.")
    else:
        print("No existe esa reserva.")

sistema_reservas()