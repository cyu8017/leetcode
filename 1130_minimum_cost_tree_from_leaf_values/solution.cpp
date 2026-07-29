// LeetCode 1130 - Minimum Cost Tree From Leaf Values
// https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int mctFromLeafValues(std::vector<int>& arr) {
        std::vector<int> stack{INT_MAX};
        int ans = 0;
        for (int x : arr) {
            while (stack.back() <= x) {
                const int mid = stack.back();
                stack.pop_back();
                ans += mid * std::min(stack.back(), x);
            }
            stack.push_back(x);
        }
        while (stack.size() > 2) {
            const int mid = stack.back();
            stack.pop_back();
            ans += mid * stack.back();
        }
        return ans;
    }
};
