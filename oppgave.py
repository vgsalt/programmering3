import click
from PIL import Image, ImageOps, ImageDraw, ImageFont
import pilgram
import pilgram.css

@click.group()
def commands():
    """Enkelt bildeprogram"""
    pass

@click.command()
@click.option('--image', help="Bilde som skal brukes", prompt=True)
@click.option('--filter', help="Hvilket filter som skal brukes. Tilgjengelige filtere: brooklyn, contrast og rise", prompt=True)
def applyfilter(image, filter):
    """Putt på et filter!"""
    with Image.open(image) as im:
        if filter == "brooklyn":
            pilgram.brooklyn(im).show()
        elif filter == "contrast":
            pilgram.css.contrast(im).show()
        elif filter == "rise":
            pilgram.rise(im).show()
        else:
            print("Ingen filter angitt / filteret er ikke i lista. Du kan velge mellom: brooklyn, contrast og rise.")
            im.show()

@click.command()
@click.option('--image', help="Bilde som skal brukes", prompt=True)
@click.option('--deg', help="Hvor mange grader bildet skal roteres. Ikke skriv '90 grader' eller '90deg' eller noe sånt", prompt=True)
def rotate(image, deg):
    """Snu bildet noen grader"""
    with Image.open(image) as im:
        im.rotate(int(deg)).show()

@click.command()
@click.option('--image', help="Bilde som skal brukes", prompt=True)
@click.option('--width', help="Bredde", prompt=True)
@click.option('--height', help="Høyde", prompt=True)
def resize(image, width, height):
    """Gjør bildet litt mindre eller større. Ditt valg!"""
    with Image.open(image) as im:
        im.resize((int(width), int(height))).show()


@click.command()
@click.option('--image', help="Bildet som skal brukes", prompt=True)
@click.option('--type', help="Hva bildet skal se ut som. Valg: square, landscape, portrait, story", prompt=True)
def cropforinsta(image, type):
    """Beskjær bildet etter instagram sine krav"""
    with Image.open(image) as im:
        if type == "square":
            im.thumbnail((500, 500), Image.LANCZOS)
            im.show()
        elif type == "landscape":
            im.thumbnail((1080, 608), Image.LANCZOS)
            im.show()
        elif type == "portrait":
            im.thumbnail((1080, 1350), Image.LANCZOS)
            im.show()
        elif type == "story":
            # Dette skal beholde bildeformatet
            # https://stackoverflow.com/a/4271003
            im.thumbnail((1080, 1920), Image.LANCZOS)
            im.show()
        else:
            print("Ukjent type.")

@click.command()
@click.option('--image', help="Bildet som skal brukes", prompt=True)
def vintageify(image):
    """Få bildet til å se litt gammelt ut 😎🧓🏻"""
    with Image.open(image) as im:
        # 1977 ser litt vintage ut
        im = pilgram._1977(im)
        im.thumbnail((500, 500), Image.LANCZOS)
        # topp, høyre, bunn og venstre
        border = (20, 20, 20, 120)
        # Farge rundt bildet
        farge = "#EDD9E8"
        nytt_bilde = ImageOps.expand(im, border=border, fill=farge)

        nytt_bilde.show()

@click.command()
@click.option('--image', help="Bildet som skal brukes", prompt=True)
@click.option('--text', help="Tekst som skal på bildet", prompt=True)
def tekst(image, text):
    """Putt på litt tekst på bildet"""
    with Image.open(image) as im:
        # Tegn den greia vi gjorde i vintageify
        im.thumbnail((500, 500), Image.LANCZOS)
        border = (20, 20, 20, 120)
        farge = "#EDD9E8"
        nytt_bilde = ImageOps.expand(im, border=border, fill=farge)

        # Tegn tekst
        font = ImageFont.truetype("Afacad-VariableFont_wght.ttf", 30)
        ImageDraw.Draw(
            nytt_bilde
        ).text(
            (20, 560),
            text,
            (0, 0, 0),
            font=font,
        )

        nytt_bilde.show()

# Legg til alle kommandoene
commands.add_command(tekst)
commands.add_command(vintageify)
commands.add_command(rotate)
commands.add_command(applyfilter)
commands.add_command(resize)
commands.add_command(cropforinsta)

# Når du kjører oppgave.py så kjører den commands()
if __name__ == '__main__':
    commands()