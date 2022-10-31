from certificado import ImageText
from PIL import Image, ImageDraw, ImageFont


color = (0, 0, 0) 

text = "Certificamos que $bFulana $bSantos $bda $bSilva, CPF $b101.555.413-59, participou, como CURSISTA, do Projeto de extensão contínuo $bROBÓTICA $bCOMO $bUMA $bINTERVENÇÃO $bSOCIAL: $bROBÓTICA $bVOLTADO $bAO $bAGRO, coordenado por FELIPE GONÇALVES DOS SANTOS, selecionado através do $bEDITAL $bNo $b03/2020/PROEN/IFS $b- $bPROGRAMA $bINSTITUCIONAL $bDE $bPESQUISA $bMULTIDISCIPLINAR $bDE $bAPOIO $bAO $bENSINO, no período de 29/08/2022 a 16/09/2022, com uma carga horária total de 40 horas."
txt2 = text.replace('$b', '')
font = 'freemomo/FreeMono.ttf'
img = ImageText('img6.jpg') # 200 = alpha


img.write_text_box((2500-135-2000-135, 800),txt2 , box_width=2000, font_filename=font,
                   font_size=40, color=color, place='justify')

t = "Corrente - PI, 16 de Setembro de 2022."

x, y = img.get_text_size(font_filename=font, font_size=40, text=t)
pos = 2500 // 2
k = x // 2
pos = pos - k
print(pos)

img.write_text_box((pos, 1100), box_width=912, font_filename=font, font_size=40, color=color, text=t)
esc = "IFPI - Campus Corrente"

l1 = "_______________________________"


img.write_text_box((400, 1300), box_width=600, font_filename=font, font_size=40, color=color, text=l1, place='center')
img.write_text_box((400, 1350), box_width=600, font_filename=font, font_size=40, color=color, text="Wellington Santos", place='center')
img.write_text_box((400, 1400), box_width=600, font_filename=font, font_size=40, color=color, text="Diretor", place='center')
img.write_text_box((400, 1450), box_width=600, font_filename=font, font_size=40, color=color, text=esc, place='center')

img.write_text_box((1500, 1300), box_width=600, font_filename=font, font_size=40, color=color, text=l1, place='center')
img.write_text_box((1500, 1350), box_width=600, font_filename=font, font_size=40, color=color, text="João Da Cunha", place='center')
img.write_text_box((1500, 1400), box_width=600, font_filename=font, font_size=40, color=color, text="Cordenador", place='center')
img.write_text_box((1500, 1450), box_width=600, font_filename=font, font_size=40, color=color, text=esc, place='center')


img.show()

# img.save('sample-imagetext.png')