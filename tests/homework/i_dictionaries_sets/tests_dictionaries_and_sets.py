#
from src.homework.i_dictionaries_sets.dictionary import get_p_distance_matrix
from src.homework.i_dictionaries_sets.dictionary import get_p_distance

baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])   

class test_config(unittest.TestCase):

     def test_intersection(self):
         self.assertEqual(baseball.intersection(basketball),set(["Carmen","Alicia"]))
         print(baseball.intersection(basketball))

     def test_union(self):
         self.assertEqual(baseball.union(basketball),set(['Jodi', 'Aida', 'Alicia','Eva', 'Carmen', 'Sarah']))
         print(baseball.union(basketball))

     def test_difference(self):
         self.assertEqual(baseball.difference(basketball),set(['Jodi','Aida']))
         print(baseball.difference(basketball))

     def test_difference2(self):
         self.assertEqual(basketball.difference(baseball),set(["Eva","Sarah"]))
         self.assertEqual(baseball.difference(basketball),set(['Jodi','Aida']))

         print(basketball.difference(baseball))
         print(baseball.difference(basketball))

     def test_symmetric(self):
         self.assertEqual(basketball.symmetric_difference(baseball),set(["Eva","Sarah",'Jodi','Aida']))
         print(basketball.symmetric_difference(baseball))