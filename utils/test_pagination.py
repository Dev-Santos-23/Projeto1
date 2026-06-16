from unittest import TestCase
from pagination import make_pagination_range

class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_pages = 4,
            current_page = 1,
        )["pagination"]
        self.assertEqual([1, 2, 3, 4], pagination)
        
    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):
        # Current Page = 1 - Qty Page = 2 - Middle Page = 2
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_pages = 4,
            current_page = 1,
        )["pagination"]
        self.assertEqual([1, 2, 3, 4], pagination)
                     
        # Current Page = 2 - Qty Page = 2 - Middle Page = 2
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_pages = 4,
            current_page = 2,
        )["pagination"]
        self.assertEqual([1, 2, 3, 4], pagination)
        
        # Current Page = 3 - Qty Page = 2 - Middle Page = 2
        # Here Range should change        
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_pages = 4,
            current_page = 3,
        )["pagination"]
        self.assertEqual([2, 3, 4, 5], pagination)
        
    def test_make_sure_middle_ranges_are_correct(self):
        # Current Page = 12 - Qty Page = 2 - Middle Page = 2
        # Here Range should change        
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_pages = 4,
            current_page = 10,
        )["pagination"]
        self.assertEqual([9, 10, 11, 12], pagination)                          

        # Current Page = 14- Qty Page = 2 - Middle Page = 2
        # Here Range should change        
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_pages = 4,
            current_page = 12,
        )["pagination"]
        self.assertEqual([11, 12, 13, 14], pagination)
        
    def test_make_pagination_range_is_static_when_last_page_is_next(self):
                     
        # Current Page = 18- Qty Page = 2 - Middle Page = 2
        # Here Range should change        
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_pages = 4,
            current_page = 18,
        )["pagination"]
        self.assertEqual([17, 18, 19, 20], pagination)
                              
        # Current Page = 19- Qty Page = 2 - Middle Page = 2
        # Here Range should change        
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_pages = 4,
            current_page = 19,
        )["pagination"]
        self.assertEqual([17, 18, 19, 20], pagination)                      

        # Current Page = 20- Qty Page = 2 - Middle Page = 2
        # Here Range should change        
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_pages = 4,
            current_page = 20,
        )["pagination"]
        self.assertEqual([17, 18, 19, 20], pagination)        


        # Current Page = 21- Qty Page = 2 - Middle Page = 2
        # Here Range should change        
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_pages = 4,
            current_page = 21,
        )["pagination"]
        self.assertEqual([17, 18, 19, 20], pagination)         