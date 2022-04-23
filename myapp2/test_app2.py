
# Create your tests here.
import pytest

def test_set_check_password1(user_1):
    print("check user1")
    assert user_1.username == "test-user"

def test_set_check_password2(user_1):
    print("check user2")
    assert user_1.username == "test-user"




# @pytest.fixture
# def fixture_1():
#     print('run-fixture-1')
#     return 1

# def test_article(fixture_1):
#     print('run-example-1')
#     num = fixture_1
#     assert num == 1