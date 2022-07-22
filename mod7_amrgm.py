import unittest
import main
import getStockSymbol

class test_main(unittest.TestCase):

    def test_getStockSymbol(self):
        input1 = "GGGFD"
        result = getStockSymbol.getStockSymbol(input1)
        self.assertEqual(result, True)
        input2 = "Gff$"
        result2 = getStockSymbol.getStockSymbol((input2))
        self.assertEqual(result2, False)
        #self.assertFalse(result, "test failed")

    def test_get_chart_type(self):
        result  = main.get_chart_type("1")
        self.assertEqual(result, "1")
        result2 = main.get_chart_type("3")
        self.assertFalse(result2)

    def test_get_time_series(self):
        result = main.get_time_series("2")
        self.assertTrue(result)
        result2 = main.get_time_series("6")
        self.assertFalse(result2)

    def test_get_beginning_date(self):
        result = main.get_beginning_date("2002-01-01")
        self.assertTrue((result))
        result2 = main.get_beginning_date("09842082")
        self.assertFalse(result2)

    def test_get_end_date(self, beginning_date = "2002-01-01"):
        beginning_date = "2002-01-01"
        result = main.get_end_date(beginning_date, "2002-02-02")
        self.assertTrue(result)
        result2 = main.get_end_date(beginning_date, "1999-02-02")
        self.assertFalse(result2)









if __name__ == '__main__':
    unittest.main()
