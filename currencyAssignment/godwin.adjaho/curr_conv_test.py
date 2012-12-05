import unittest
import pickle
from curr_conv import calc_exchange
import re

class TestCurrencyConvert(unittest.TestCase):

    def runTest(self):
        self.testline0()
        self.testorder()
        self.testexchangerate()
        self.testnumgerformat()

    def setUp(self):
        self.ghs = ['Rate: GHS',
                    '',
                    '1 GHS is',
                    'AUD 0.504 Australian Dollar',
                    'CAD 0.522 Canadian Dollar',
                    'EGP 3.200 Egyption Pound',
                    'EUR 0.406 Euro',
                    'GBP 0.329 British Pound',
                    'INR 29.300 Indian Rupee',
                    'NGN 82.800 Nigerian Naira',
                    'USD 0.527 US Dollar',
                    'ZAR 4.680 South African Rand']

        self.aud = ['Rate: AUD',
                    '',
                    '1 AUD is',
                    'CAD 1.036 Canadian Dollar',
                    'EGP 6.349 Egyption Pound',
                    'EUR 0.806 Euro',
                    'GBP 0.653 British Pound',
                    'GHS 1.984 Ghana Cedi',
                    'INR 58.135 Indian Rupee',
                    'NGN 164.286 Nigerian Naira',
                    'USD 1.046 US Dollar',
                    'ZAR 9.286 South African Rand']
        
        self.usd = ['Rate: USD',
                    '',
                    '1 USD is',
                    'AUD 0.956 Australian Dollar',
                    'CAD 0.991 Canadian Dollar',
                    'EGP 6.072 Egyption Pound',
                    'EUR 0.770 Euro',
                    'GBP 0.624 British Pound',
                    'GHS 1.898 Ghana Cedi',
                    'INR 55.598 Indian Rupee',
                    'NGN 157.116 Nigerian Naira',
                    'ZAR 8.880 South African Rand']


    def testline0(self):
        '''Makes sure that line0 returns the correct rate.
        '''
        msg = 'Check the first line'
        self.assertIn('USD',calc_exchange('USD')[0],msg)
        self.assertIn('AUD',calc_exchange('AUD')[0],msg)
        self.assertIn('GHS',calc_exchange('GHS')[0],msg)

    def testorder(self):
        ''' Tests that the lines are in alphabetical order
        '''
        msg = 'Have you sorted your output?'
        rates = calc_exchange('USD')
        prevRate = rates[3]
        for rate in rates[4:]:
            self.assertTrue(rate > prevRate,msg)
            prevRate = rate
            
    def testexchangerate(self):
        '''Tests a few exchange rates
        '''
        msg = 'Check your exchange rates'
        rates = calc_exchange('USD')
        for rate in rates:
            if rate.startswith('NGN'):
                self.assertIn('157.116',rate,msg)
            if rate.startswith('EUR'):
                self.assertIn('0.770',rate,msg)

    def testnumberformat(self):
        '''Tests that all numbers are in the %0.3f format
        '''
        msg = 'How are you printing your numbers?'
        for rate in calc_exchange('USD')[4:]:
            m = re.search('([\d\.]+)',rate)
            if m:
                self.assertRegexpMatches(m.group(),'\d*\.\d{3}',msg)

def get_failures():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCurrencyConvert)
    testResults = unittest.TextTestRunner(verbosity=0).run(suite)
    return [f[1].strip().split('\n')[-1] for f in testResults.failures]

def main():
    print '\n'.join(get_failures())

if __name__ == '__main__':
    main()