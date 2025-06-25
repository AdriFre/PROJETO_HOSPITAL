from modules.Hospital import PacientesCancer

def main():
    paciente1 = PacientesCancer("000.A", "Antonia", "26/06/1958", "12/05/2025")
    print(paciente1.registro, paciente1.nome)
    print(paciente1.status_prazo())  

    paciente2 = PacientesCancer("0001.A", "Berenice", "15/10/1990", "01/03/2025")
    print(paciente2.registro, paciente2.nome)
    print(paciente2.status_prazo())

    paciente3 = PacientesCancer("0002.A", "Carla", "15/03/1998", "01/03/2025", "05/04/2025")
    print(paciente3.registro, paciente3.nome)
    print(paciente3.status_prazo())

    paciente4 = PacientesCancer("0003.A", "Regina", "10/03/1985", "01/03/2025", "11/06/2025")
    print(paciente4.registro, paciente4.nome)
    print(paciente4.status_prazo())
if __name__ == "__main__":
    main()