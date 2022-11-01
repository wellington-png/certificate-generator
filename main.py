from certificado import Certificado


text = """Certificamos que Fulana Santos da Silva, CPF 101.555.413-59, participou, como CURSISTA, do Projeto de
extensão contínuo ROBÓTICA COMO UMA INTERVENÇÃO SOCIAL: ROBÓTICA VOLTADO AO AGRO,
coordenado por FELIPE GONÇALVES DOS SANTOS, selecionado através do EDITAL No 03/2020/PROEN/IFS -
PROGRAMA INSTITUCIONAL DE PESQUISA MULTIDISCIPLINAR DE APOIO AO ENSINO, no período de
29/08/2022 a 16/09/2022, com uma carga horária total de 40 horas."""

t = Certificado()
t.create_main_text(text, 40)
t.create_date_city('Corrente - PI, 16 de Setembro de 2022.')
t.right_signature('Jose Wellington', 'Cordenador', 'IFPI campos corrente')
t.left_signature('Jose Wellington', 'Cordenador', 'IFPI campos corrente')
t.show()
t.save('wellington')
