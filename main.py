from curso import Curso

c = Curso(
    curso="ROBÓTICA COMO UMA INTERVENÇÃO SOCIAL: ROBÓTICA VOLTADO AO AGRO",
    carga=40,
    data_start="29/08/2022",
    date_end="16/09/2022",
    edital="EDITAL No 03/2020/PROEN/IFS - PROGRAMA INSTITUCIONAL DE PESQUISA MULTIDISCIPLINAR DE APOIO AO ENSINO",
    coordenado="FELIPE GONÇALVES DOS SANTOS",
)
c.path_file_csv = 'alunos.csv'
c.gerar_certificados('Corrente - PI', 'Israel Lobato Rocha', 'IFPI - Campus Corrente')

# n = 'ROBÓTICA COMO UMA INTERVENÇÃO SOCIAL: ROBÓTICA VOLTADO AO AGRO'
# print(f'$b{n.replace(" ", " $b")}')
