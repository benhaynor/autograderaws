'''
author: Ben Haynor
Date: Nove 27-2012
'''
import csv
import pickle

def calc_exchange(currency):
    converter = Converter()
    return converter.rates(currency)
    

class Converter:
    
    def __init__(self):
        self.__rates = self.__load_rates()
        self.__rates.sort()
        self.__rate_dict = {rateTuple[0]: rateTuple for rateTuple in self.__rates}
    
    def getRates(self):
        return self.__rates

    def __load_rates(self):
        '''
        Loads currency rates, stores it in the private
        rates list
        '''
        rates = []
        with open('rates.txt') as f:
            for line in f:
                rates.append(line.strip().split(','))
        return rates
    
    def rates(self,currency):
        ''' Return
        '''
        value = float(self.__rate_dict[currency][1])
        out = ['Rate: %s' % currency]
        out.append('')
        out.append('1 %s is' % currency)
        #out = 'Rate: %s\n\n1 %s is\n\n' % (currency, self.__rate_dict[currency][2])
        for cur, val, curName in self.__rates:
            if cur != currency:
                out.append('%s %0.3f %s' % (cur, float(val) / value, curName))
        return out
        
def main():
    converter = Converter()
    print '\n'.join(converter.rates('USD'))

if __name__ == "__main__":
    main()
