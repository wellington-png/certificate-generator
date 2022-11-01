from datetime import datetime

from certificado import Certificado


class Curso:

    messes = [
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'
    ]

    data_atual = datetime.now()

    def __init__(self, curso, carga, data_start, date_end, edital, coordenado) -> None:
        self.curso = curso
        self.carga = carga
        self.data_start = data_start
        self.date_end = date_end
        self.edital = edital
        self.coordenado = coordenado
        self.path_file_csv = None
        self.certificados = []

    def gerar_certificados(self, cidade, diretor, campos):
        cert = Certificado()

        cert.create_main_text(
            curso=self.curso,
            name="Wellington santos Nascimento",
            carga=self.carga,
            date_start=self.data_start,
            date_end=self.date_end,
            edital=self.edital,
            coordenador=self.coordenado,
            cpf="xxx.xxx.xxx-xx",
        )
        dia = self.data_atual.day
        mes = self.data_atual.month
        ano = self.data_atual.year

        city_date = f'{cidade}, {dia} de {self.messes[mes-1]} de {ano}.'
        cert.create_date_city(city_date)

        cert.left_signature(self.coordenado, 'Coordenador', campos)
        cert.right_signature(diretor, 'Diretor', campos)

        self.certificados.append(cert)
        cert.save_image("wellington")


if __name__ == '__main__':
    c = Curso(
        curso="ROBÓTICA COMO UMA INTERVENÇÃO SOCIAL: ROBÓTICA VOLTADO AO AGRO",
        carga=40,
        data_start="29/08/2022",
        date_end="16/09/2022",
        edital="EDITAL No 03/2020/PROEN/IFS - PROGRAMA INSTITUCIONAL DE PESQUISA MULTIDISCIPLINAR DE APOIO AO ENSINO",
        coordenado="FELIPE GONÇALVES DOS SANTOS",
    )
    c.gerar_certificados('Corrente - PI', 'Israel Lobato Rocha', 'IFPI - Campus Corrente')
