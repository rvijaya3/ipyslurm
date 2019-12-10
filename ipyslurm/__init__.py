from .ipyslurm import IPySlurm

__version__ = '1.5.0'


def load_ipython_extension(ipython):
    ipython.register_magics(IPySlurm)
