# Imports
from time import sleep

# Progress bar for finite loops
class ProgressBar:
    colors = {'red': '\033[91m',
              'green': '\033[92m',
              'blue': '\033[94m',
              'yellow': '\033[93m',
              'purple': '\033[95m',
              'white': '\033[0m',
              'black': '\033[90m'}

    def __init__(self, listLength, kvPairs):
        self.currentIndex = 0
        self.listLength = listLength
        self.kvPairs = kvPairs

    def __next__(self):
        barLength = self.kvPairs['length']
        ratio = (len(str(self.listLength)) - len(str(self.currentIndex + 1))) * ' ' + f'{self.currentIndex + 1}/{self.listLength}'
        percentage = f'{int(100 * (self.currentIndex + 1) / self.listLength)}% '

        spacesInFront = (5 - len(str(percentage))) * ' '
        barStart = '│'
        barSymbol = '█'
        barFilled = int((self.currentIndex + 1) * barLength / self.listLength)
        barEmpty = barFilled * barSymbol + (barLength - barFilled) * ' '
        barEnd = '│ '

        print('\r', end=' ')
        print(self.colors[self.kvPairs['color']] + self.kvPairs['text'] + spacesInFront + percentage + barStart + barEmpty + barEnd + ratio, end='')
        if self.currentIndex == self.listLength - 1:
            print('\033[0m', end='\n')

        sleep(self.kvPairs['sleep'])

        self.currentIndex += 1

        return self.currentIndex

    __call__ = __next__

def progressbar(listLength, **kwargs):
    kvPairs = {'color': 'white',
               'text': '',
               'length': 30,
               'sleep': 0}
    for key, value in kwargs.items():
        kvPairs[key] = value

    myProgressbar = iter(ProgressBar(listLength, kvPairs), listLength)

    return myProgressbar


if __name__ == '__main__':
    print('This is my progressbar:')
    for i in progressbar(5, color='red', text='Progression: ', length=40, sleep=1):
        pass
    print('Done!')
