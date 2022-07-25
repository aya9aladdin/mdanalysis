
from .base import GuesserBase
from .DefaultGuesser import DefaultGuesser

# guessers dictionary mimic registaration by metaclass
GUESSERS = {'DEFAULT': DefaultGuesser}


def get_guesser(a, context):
    """get an appropiate guesser to the universe and pass
       the atomGroup of the universe to the guesser

    Parameters
    ----------
    atoms: AtomGroup of the universe
    context: string or Guesser class
    Returns
    -------
    Guesser class
    """
    if isinstance(context, GuesserBase):
        return context
    try:
        guesser = GUESSERS[context.upper()](a)
    except KeyError:
        raise TypeError("Unidentified guesser type {0}".format(context))
    return guesser
