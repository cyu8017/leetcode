// LeetCode 0728 - Self Dividing Numbers
// https://leetcode.com/problems/self-dividing-numbers/

#include <vector>

class Solution {
public:
    std::vector<int> selfDividingNumbers(int left, int right) {
        std::vector<int> result;
        for (int num = left; num <= right; ++num) {
            if (isSelfDividing(num)) {
                result.push_back(num);
            }
        }
        return result;
    }

private:
    bool isSelfDividing(int num) {
        int x = num;
        while (x) {
            int digit = x % 10;
            if (digit == 0 || num % digit != 0) {
                return false;
            }
            x /= 10;
        }
        return true;
    }
};
