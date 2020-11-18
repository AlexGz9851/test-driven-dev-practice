import unittest
from my_list import MyList

class TestStringMethods(unittest.TestCase):
    """
        Realizar 3 unit tests por cada uno de los siguientes requerimientos para una lista:

        We need to get the size of the list
        We need to clear the list
        We need to add Items
        We need to be able to check if an item exists
        We need to get elements by index
        We need to search the index of an object
        We need to remove an item by index
    """

    @classmethod
    def setUpClass(self):
        self.myList1 = MyList((4, 5, 6,))
        self.myList2 = MyList(tuple())
        self.myList3 = MyList(("x",4,"que","Hola",))
        self.myList4 = MyList(("x",4,"que",))
        self.myList5 = MyList(("x",))
        self.myList6 = MyList((4, 4, 4, 4, 4, 4,))
        self.myList11 = MyList(("x", 4, "que",))
        self.myList12 = MyList(("x",))
        self.myList31 = MyList(("hola","x","como","estas",))
        self.myList32 = MyList((3, "x", "como", ))
        self.myList33 = MyList(( 5,))
        self.myList34 = MyList(("hola", "x", "como", "x",))

    def test_size(self):
        self.assertEqual(len(self.myList1), 3) # Using modified __len__ function
        self.assertEqual(len(self.myList2), 0) # Using modified __len__ function
        self.assertEqual(len(self.myList3), 4) # Using modified __len__ function

    def test_clear(self):
        self.myList4.clear()
        self.assertEqual(len(self.myList4), 0)
        self.assertTrue(self.myList4._head is None)

        self.myList5.clear()
        self.assertEqual(len(self.myList5), 0)
        self.assertTrue(self.myList5._head is None)

        self.myList6.clear()
        self.assertEqual(len(self.myList6), 0)
        self.assertTrue(self.myList6._head is None)

    def test_get(self):
        self.assertEqual(self.myList1.get(-1), None)
        self.assertEqual(self.myList1.get(0), 4)
        self.assertEqual(self.myList1.get(2), 6)
        self.assertEqual(self.myList1.get(3), None)

    def test_add(self):
        new = 9
        self.myList11.add(new)
        self.assertEqual(len(self.myList11), 4)
        self.assertEqual(self.myList11.get(3), new)
        new = "yo"
        self.myList12.add(new)
        self.assertEqual(len(self.myList12), 2)
        self.assertEqual(self.myList12.get(1), new)
        new = None
        self.myList12.add(new)
        self.assertEqual(len(self.myList12), 3)
        self.assertEqual(self.myList12.get(2), new)

    def test_exists(self):
        self.assertEqual(self.myList1.exists(4), True)
        self.assertEqual(self.myList1.exists(5), True)
        self.assertEqual(self.myList1.exists(6), True)
        self.assertEqual(self.myList1.exists(8), False)
        self.assertEqual(self.myList1.exists("XX"), False)
        self.assertEqual(self.myList1.exists(None), False)

    def test_get_index_of(self):
        self.assertEqual(self.myList1.get_index_of(4), 0)
        self.assertEqual(self.myList1.get_index_of(5), 1)
        self.assertEqual(self.myList1.get_index_of(6), 2)
        self.assertEqual(self.myList1.get_index_of(8), -1)
        self.assertEqual(self.myList1.get_index_of("XX"), -1)
        self.assertEqual(self.myList1.get_index_of(None), -1)


    def test_remove(self):
        self.assertEqual(self.myList31.exists("x"), True)
        self.assertEqual(len(self.myList31), 4)
        self.assertEqual(self.myList31.remove(1), "x")
        self.assertEqual(len(self.myList31), 3)
        self.assertEqual(self.myList31.exists("x"), False)

        self.assertEqual(self.myList32.exists(3), True)
        self.assertEqual(len(self.myList32), 3)
        self.assertEqual(self.myList32.remove(7), None)
        self.assertEqual(len(self.myList32), 3)
        self.assertEqual(self.myList32.exists(3), True)

        self.assertEqual(self.myList34.get_index_of("x"), 1)
        self.assertEqual(len(self.myList34), 4)
        self.assertEqual(self.myList34.remove(1), "x")
        self.assertEqual(len(self.myList34), 3)
        self.assertEqual(self.myList34.get_index_of("x"), 2)


if __name__ == '__main__':
    unittest.main()
