from setuptools import setup, find_packages

setup(
    name="paquetecalculos",
    version="1.0",
    description="Paquete de redondeo y potencia",
    author="Miguel",
    author_email="veitne2007mtm23@gmail.com",
    url="http://www.pildorasinformaticas.es",
    packages=find_packages(include=["paquetecalculos", "paquetecalculos.*"])
)
