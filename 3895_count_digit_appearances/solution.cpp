// LeetCode 3895 - Count Digit Appearances
// https://leetcode.com/problems/count-digit-appearances/

#include <vector>

class Solution {
public:
    int countDigitOccurrences(std::vector<int>& nums, int digit) {
        int ans = 0;
        for (int x : nums) {
            for (; x > 0; x /= 10) {
                if (x % 10 == digit) ans++;
            }
        }
        return ans;
    }
};
