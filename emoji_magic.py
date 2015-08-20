from emoji import emojize

from IPython.core.magic import Magics, line_magic, magics_class


@magics_class
class EmojiMagic(Magics):
    @line_magic
    def emoji(self, line):
        print emojize(line, use_aliases=True)


def load_ipython_extension(ipython):
    ipython.register_magics(EmojiMagic)
