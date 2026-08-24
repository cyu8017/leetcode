// LeetCode 2455 - Average Value of Even Numbers That Are Divisible by Three
// https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

#include <vector>

class Solution {
public:
    int averageValue(std::vector<int>& nums) {
        int sum = 0, cnt = 0;
        for (int x : nums) {
            if (x % 6 == 0) { sum += x; cnt++; }
        }
        return cnt == 0 ? 0 : sum / cnt;
    }
};
