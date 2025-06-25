from datetime import datetime, timedelta

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