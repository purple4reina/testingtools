import sys
import colors


class ColorPrint(object):

    def __init__(self):
        self.colors = colors

    def __getattr__(self, name):
        if not name.startswith('print'):
            raise NameError('%s has no method %s' % (
                self.__module__, name))

        color = name.split('_', 1)[-1]
        return self._get_print_color_method(color)

    def _get_color_str(self, color):
        try:
            return getattr(self.colors, color.upper())
        except AttributeError:
            return ''

    def _get_print_color_method(self, color):
        def print_(val):
            print '{color}{val}{stop}'.format(
                color=self._get_color_str(color),
                val=val,
                stop=self.colors.COLOR_OFF,
            )
        return print_



sys.modules[__name__] = ColorPrint()
