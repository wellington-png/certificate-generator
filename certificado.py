import os

from PIL import Image, ImageDraw, ImageFont
import PIL
from certicado_config import CertificadoConfig


class Certificado(CertificadoConfig):
    line_signature = "_______________________________"

    def __init__(
        self,
        filename="static/img6.jpg",
        mode="RGBA",
        background=(0, 0, 0, 0),
        encoding="utf8",
    ):
        super().__init__(mode, background, encoding)
        self.filename = filename
        self.image = Image.open(self.filename)
        self.size = self.image.size
        self.background = background
        self.mode = mode
        self.draw = ImageDraw.Draw(self.image)
        self.encoding = encoding

    def save_image(self, filename=None):
        self.image.save(f"certificado/{filename}.jpg")

    def save_pdf(self, filename=None):
        self.image.save(f"certificado/{filename}.pdf")

    def show(self):
        self.image.show()

    def get_size(self):
        return self.image.size

    def create_main_text(
        self, name, curso, carga, date_start, date_end, edital, coordenador, cpf
    ):
        text = f"""Certificamos que {name}, CPF {cpf}, participou, como CURSISTA, do Projeto de
extensão contínuo {curso},
coordenado por {coordenador}, selecionado através do {edital}, no período de
{date_start} a {date_end}, com uma carga horária total de {carga} horas."""

        self.write_text_box(
            (230, 800),
            text,
            box_width=2000,
            font_filename="static/freemomo/FreeMono.ttf",
            font_size=40,
            color=self.background,
            place="justify",
        )

    def create_date_city(self, text):
        x, y = self.get_text_size(
            font="static/freemomo/FreeMono.ttf", font_size=40, text=text
        )
        pos = 2500 // 2
        k = x // 2
        pos = pos - k
        self.write_text_box(
            (pos, 1100),
            box_width=912,
            font_filename="static/freemomo/FreeMono.ttf",
            font_size=40,
            color=self.background,
            text=text,
        )

    def left_signature(self, nome, cargo, instituicao):
        self.write_text_box(
            (400, 1300),
            box_width=650,
            font_filename="static/freemomo/FreeMono.ttf",
            font_size=40,
            color=self.background,
            text=self.line_signature,
            place="center",
        )
        self.write_text_box(
            (400, 1350),
            box_width=650,
            font_filename="static/freemomo/FreeMono.ttf",
            font_size=40,
            color=self.background,
            text=nome,
            place="center",
        )
        self.write_text_box(
            (400, 1400),
            box_width=600,
            font_filename="static/freemomo/FreeMono.ttf",
            font_size=40,
            color=self.background,
            text=cargo,
            place="center",
        )
        self.write_text_box(
            (400, 1450),
            box_width=600,
            font_filename="static/freemomo/FreeMono.ttf",
            font_size=40,
            color=self.background,
            text=instituicao,
            place="center",
        )

    def right_signature(self, nome, cargo, instituicao):
        self.write_text_box(
            (1500, 1300),
            box_width=600,
            font_filename="static/freemomo/FreeMono.ttf",
            font_size=40,
            color=self.background,
            text=self.line_signature,
            place="center",
        )
        self.write_text_box(
            (1500, 1350),
            box_width=600,
            font_filename="static/freemomo/FreeMono.ttf",
            font_size=40,
            color=self.background,
            text=nome,
            place="center",
        )
        self.write_text_box(
            (1500, 1400),
            box_width=600,
            font_filename="static/freemomo/FreeMono.ttf",
            font_size=40,
            color=self.background,
            text=cargo,
            place="center",
        )
        self.write_text_box(
            (1500, 1450),
            box_width=600,
            font_filename="static/freemomo/FreeMono.ttf",
            font_size=40,
            color=self.background,
            text=instituicao,
            place="center",
        )


if __name__ == "__main__":
    t = Certificado()
    t.create_main_text(
        """Certificamos que Fulana Santos da Silva, CPF 101.555.413-59, participou, como CURSISTA, do Projeto de
extensão contínuo ROBÓTICA COMO UMA INTERVENÇÃO SOCIAL: ROBÓTICA VOLTADO AO AGRO,
coordenado por FELIPE GONÇALVES DOS SANTOS, selecionado através do EDITAL No 03/2020/PROEN/IFS -
PROGRAMA INSTITUCIONAL DE PESQUISA MULTIDISCIPLINAR DE APOIO AO ENSINO, no período de
29/08/2022 a 16/09/2022, com uma carga horária total de 40 horas.""",
        40,
    )
    t.create_date_city("Corrente - PI, 16 de Setembro de 2022.")
    t.right_signature("Jose Wellington", "Cordenador", "IFPI campos corrente")
    t.left_signature("Jose Wellington", "Cordenador", "IFPI campos corrente")
    t.show()
    t.save("wellington")
