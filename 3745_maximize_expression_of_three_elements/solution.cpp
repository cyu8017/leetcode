// LeetCode 3745 - Maximize Expression of Three Elements
// https://leetcode.com/problems/maximize-expression-of-three-elements/

#include <climits>
#include <vector>

class Solution {
public:
    int maximizeExpressionOfThree(std::vector<int>& nums) {
        const int inf = 1 << 30;
        int a = -inf, b = -inf, c = inf;
        for (int x : nums) {
            if (x < c) c = x;
            if (x >= a) { b = a; a = x; }
            else if (x > b) b = x;
        }
        return a + b - c;
    }
};
