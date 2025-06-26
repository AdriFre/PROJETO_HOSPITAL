from datetime import datetime, timedelta

class SistemaHospital:
    def __init__(self):
        self.pacientes = []
    def cadastrar_paciente(self):
        registro = input("Registro:")
        nome = input("nome:")
        nascimento = input("data de nascimento (dd/mm/aaaa):")
        diagnostico = input("data do diagnóstico (dd/mm/aaaa):")
        inicio = input("data do inicio do tratamento dd/mm/aaaa (deixe vazio se não inicio)")
        inicio = inicio if inicio.strip() != "" else None

        paciente = PacientesCancer(registro, nome, nascimento, diagnostico, inicio)
        self.pacientes.append(paciente)
        print(f"paciente {nome} cadastrada com sucesso! \n" )

    def listar_nao_iniciaram_tratamento(self):
        print("\n Pacientes que ainda não iniciaram o tratamento: \n")
        for p in self.pacientes:
            if not p.inicio_tratamento:
                print(f"- {p.nome} (diagnóstico: {p.data_diagnostico.strftime('%d/%m/%Y')})")
        print()

    def mostrar_alertas(self):
        print("\n Alertas:")
        for p in self.pacientes:
            alertas = GerenciadorAlertas.verificar_alertas(p)
            if alertas:
                print(f"\n Paciente {p.nome}:")
                for alerta in alertas:
                    print(" - ", alerta)
        print()
    
    def adicionar_procedimento(self):
        registro = input("Digite o registro do paciente: ")
        paciente = next((p for p in self.pacientes if p.registro == registro), None )
        if not paciente:
            print("Paciente não encontrada.")
            return
        print("\n 1- Início do tratamento \n 2- Consulta \n 3- Exame \n 4- Cirurgia")
        opcao = input("Escolha o procedimento:")
        data = input("Data do procedimento (dd/mm/aaaa):")

        if opcao == "1":
            paciente.inicio_tratamento = datetime.strptime(data, "%d/%m/%Y")
            print("Início do tratamento registrado!")
        elif opcao == "2":
            paciente.adicionar_consulta(data)
            print("Consulta registrada!")
        elif opcao == "3":
            nome_exame = input("Nome do exame:")
            paciente.adicionar_exame(nome_exame, data)
            print("Exame registrado!")
        elif opcao == "4":
            print("Cirurgia")
        else:
            print("opção inválida")
        print()
class PacientesCancer:
    def __init__(self, registro, nome, data_nascimento, data_diagnostico, inicio=None):
        self.registro = registro
        self.nome = nome
        self.data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
        self.data_diagnostico = datetime.strptime(data_diagnostico, "%d/%m/%Y")
        self.inicio_tratamento = datetime.strptime(inicio, "%d/%m/%Y") if inicio else None
        self.consulta = []
        self.exames = []

    def calcular_prazo(self):
        return self.data_diagnostico + timedelta(days=60)

    def status_prazo(self):
        prazo = self.calcular_prazo()
        hoje = datetime.today()

        if self.inicio_tratamento:
            if self.inicio_tratamento <= prazo:
                return f"{self.nome} iniciou o tratamento dentro do prazo"
            else:
                atraso = (self.inicio_tratamento - prazo).days
                return f"{self.nome} iniciou o tratamento com {atraso} dias de atraso"
        else:
            if hoje <= prazo:
                dias = (prazo - hoje).days
                return f"{self.nome} ainda está no prazo, a paciente possui {dias} dias para começar o tratamento"
            else:
                dias = (hoje - prazo).days
                return f"{self.nome} está com {dias} dias de atraso para o início do tratamento"

    def adicionar_consulta(self, data):
        self.consulta.append(datetime.strptime(data, "%d/%m/%Y"))

    def adicionar_exames(self, nome, data_prevista):
        self.exames.append({"nome": nome, "data_prevista": datetime.strptime(data_prevista, "%d/%m/%Y")})


class GerenciadorAlertas:
    @staticmethod
    def verificar_alertas(paciente: PacientesCancer):
        hoje = datetime.today()
        alertas = []

        prazo_final = paciente.calcular_prazo()
        dias_restantes = (prazo_final - hoje).days

        alertas.append(paciente.status_prazo())

        if not paciente.inicio_tratamento and dias_restantes == 7:
            alertas.append(f"Aviso: faltam apenas 7 dias para o prazo do inicio do tratamento de {paciente.nome} (prazo: {prazo_final.strftime('%d/%m/%Y')})")

        return alertas
    

def menu():
    sistema = SistemaHospital()

    while True:
        print("\nMenu:")
        print("1. Cadastrar paciente")
        print("2. Ver pacientes sem início de tratamento")
        print("3. Ver alertas")
        print("4. Adicionar procedimento")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sistema.cadastrar_paciente()
        elif opcao == "2":
            sistema.listar_nao_iniciaram_tratamento()
        elif opcao == "3":
            sistema.mostrar_alertas()
        elif opcao == "4":
            sistema.adicionar_procedimento()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()