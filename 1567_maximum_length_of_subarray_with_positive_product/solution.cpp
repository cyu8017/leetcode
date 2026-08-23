// LeetCode 1567 - Maximum Length of Subarray With Positive Product
// https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

#include <algorithm>
#include <vector>

class Solution {
public:
    int getMaxLen(std::vector<int>& nums) {
        int positive = 0;
        int negative = 0;
        int answer = 0;
        for (int x : nums) {
            if (x == 0) {
                positive = negative = 0;
            } else if (x > 0) {
                ++positive;
                negative = negative ? negative + 1 : 0;
            } else {
                const int new_positive = negative ? negative + 1 : 0;
                const int new_negative = positive + 1;
                positive = new_positive;
                negative = new_negative;
            }
            answer = std::max(answer, positive);
        }
        return answer;
    }
};
