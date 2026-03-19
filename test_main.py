import pytest
from solve1 import solve1
from solve2 import solve2

class TestSolve1:
    def test_basic_case(self):
        # 기본 예시: 3(홀수), 9(홀수) -> 12
        assert solve1([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 12

    def test_no_match(self):
        # 3의 배수 중 홀수가 없는 경우 -> 0
        assert solve1([2, 4, 6, 8, 10]) == 0

    def test_all_match(self):
        # 모두 3의 배수이면서 홀수인 경우 -> 3 + 9 + 15 = 27
        assert solve1([3, 6, 9, 12, 15]) == 27

    def test_duplicates(self):
        # 중복된 값이 있는 경우 -> 15 + 15 + 15 = 45
        assert solve1([15, 15, 15]) == 45

class TestSolve2:
    def test_basic_NN(self):
        # 기본 예시 1
        assert solve2("NN") == 90

    def test_basic_CN(self):
        # 기본 예시 2
        assert solve2("CN") == 260

    def test_basic_CCN(self):
        # 기본 예시 3
        assert solve2("CCN") == 6500

    def test_complex_format(self):
        # 복잡한 조합 (C 26 * N 10 * N 9 * C 26)
        assert solve2("CNNC") == 60840
        
    def test_same_four(self):
        # 같은 형식이 4번 연속 등장 (N 10 * N 9 * N 9 * N 9)
        assert solve2("NNNN") == 7290
