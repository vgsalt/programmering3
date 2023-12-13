import click
from PIL import Image
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
            print("Ingen filter angitt")
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

commands.add_command(rotate)
commands.add_command(applyfilter)
commands.add_command(resize)

if __name__ == '__main__':
    commands()