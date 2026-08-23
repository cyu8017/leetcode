// LeetCode 2443 - Sum of Number and Its Reverse
// https://leetcode.com/problems/sum-of-number-and-its-reverse/

class Solution {
public:
    bool sumOfNumberAndReverse(int num) {
        auto rev = [](int x) {
            int r = 0;
            while (x > 0) {
                r = r * 10 + x % 10;
                x /= 10;
            }
            return r;
        };
        for (int i = 0; i <= num; i++) {
            if (i + rev(i) == num) return true;
        }
        return false;
    }
};
