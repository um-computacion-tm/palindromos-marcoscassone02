import unittest
from palindromo import palindromo
class TestContadorLetras(unittest.TestCase):
    def test_neuquen(self):
        resultado = palindromo("neuquen")
        self.assertEqual(resultado,True)
    def test_ojorojo(self):
        resultado = palindromo("ojo rojo")
        self.assertEqual(resultado,True)
    def test_unolargo(self):
        resultado = palindromo("Somos o no somos")
        self.assertEqual(resultado,True)
if __name__ == '__main__':
    unittest.main()
            
        
    
    