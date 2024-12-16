import pytest
from Stack import Stack  # Replace with the actual module path if different


class TestStack:
    def test_initialize_stack(self):
        """Test Stack initialization with and without items."""
        stk1 = Stack()  # Default initialization
        assert stk1.size() == 0
        assert stk1.empty() is True

        stk2 = Stack([1, 2, 3])  # Initialize with items
        assert stk2.size() == 3
        assert stk2.empty() is False

    def test_push(self):
        """Test pushing elements onto the stack."""
        stk = Stack([], 2)  # Stack with a limit of 2
        stk.push(1)
        assert stk.size() == 1
        assert stk.search(1) == 1  # 1 is on top of the stack

        stk.push(2)
        assert stk.size() == 2
        assert stk.search(2) == 1  # 2 is now on top of the stack

        with pytest.raises(OverflowError, match="Stack is full"):
            stk.push(3)  # Should raise an OverflowError

    def test_pop(self):
        """Test popping elements off the stack."""
        stk = Stack([1, 2, 3])
        assert stk.pop() == 3  # Top element
        assert stk.size() == 2

        assert stk.pop() == 2
        assert stk.pop() == 1
        assert stk.empty() is True

        with pytest.raises(IndexError, match="Pop from empty stack"):
            stk.pop()  # Should raise an IndexError

    def test_size(self):
        """Test size() method."""
        stk = Stack([1, 2])
        assert stk.size() == 2
        stk.pop()
        assert stk.size() == 1
        stk.push(3)
        assert stk.size() == 2

    def test_empty(self):
        """Test empty() method."""
        stk = Stack()
        assert stk.empty() is True
        stk.push(1)
        assert stk.empty() is False
        stk.pop()
        assert stk.empty() is True

    def test_full(self):
        """Test full() method."""
        stk = Stack([1], 1)  # Stack initialized with limit 1
        assert stk.full() is True
        assert stk.size() == 1

        stk.pop()
        assert stk.full() is False
        stk.push(1)
        with pytest.raises(OverflowError, match="Stack is full"):
            stk.push(2)  # Should raise an OverflowError

    def test_search(self):
        """Test search() method to find elements in the stack."""
        stk = Stack([1, 2, 3])
        assert stk.search(3) == 1  # 3 is on top, distance 1
        assert stk.search(2) == 2  # 2 is below top, distance 2
        assert stk.search(1) == 3  # 1 is at the bottom, distance 3
        assert stk.search(4) == -1  # 4 is not in the stack
