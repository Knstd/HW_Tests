import unittest
from unittest import mock

from parameterized import parameterized
from Task_1.secretary import *


class Tests(unittest.TestCase):

    @parameterized.expand([
        ["2207 876234", documents, True],
        ["10006", documents, True],
        ["11-2", documents, True],
        ["2207", documents, False]
    ])
    def test_check_document_existance(self, test_data_1, test_data_2, result):
        self.assertEqual(check_document_existance(test_data_1, test_data_2), result)

    @parameterized.expand([
        ["10006", documents, "Аристарх Павлов"],
        ["11-2", documents, "Геннадий Покемонов"],
        ["112", documents, "Not exist"],
    ])
    def test_get_doc_owner_name(self, test_data_1, test_data_2, result):
        self.assertEqual(get_doc_owner_name(test_data_1, test_data_2), result)

    def test_get_all_doc_owners_names(self):
        self.assertEqual(get_all_doc_owners_names(documents),
                         {'Геннадий Покемонов', 'Василий Гупкин', 'Аристарх Павлов'})

    @parameterized.expand([
        ['5455 028765', directories, 'Removed succuseful'],
        ["11-2", directories, 'Removed succuseful'],
        ['100006', directories, 'Not exist'],
    ])
    def test_remove_doc_from_shelf(self, test_data_1, test_data_2, result):
        self.assertEqual(remove_doc_from_shelf(test_data_1, test_data_2), result)

    @parameterized.expand([
        ['4', ('4', True)],
        ['7', ('7', True)],
        ['1', ('1', False)],
    ])
    def test_add_new_shelf(self, test_data, result):
        self.assertEqual(add_new_shelf(test_data), result)

    def test_append_doc_to_shelf(self):  # ?
        self.assertEqual(append_doc_to_shelf('123', '4', directories), 'Done')

    @mock.patch('Task_1.secretary.check_document_existance', return_value=True)
    def test_get_doc_shelf(self, mock_check_document_existance):
        self.assertEqual(get_doc_shelf('11-2', documents, directories), '1')
        mock_check_document_existance.assert_called_once_with("11-2", documents)


if __name__ == '__main__':
    unittest.main()
