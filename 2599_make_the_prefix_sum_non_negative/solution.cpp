// LeetCode 2599 - Make the Prefix Sum Non-negative
// https://leetcode.com/problems/make-the-prefix-sum-non-negative/

#include <queue>
#include <vector>

class Solution {
public:
    int makePrefSumNonNegative(std::vector<int>& nums) {
        std::priority_queue<int, std::vector<int>, std::greater<int>> h;
        long long sum = 0;
        int ans = 0;
        for (int x : nums) {
            sum += x;
            if (x < 0) h.push(x);
            if (sum < 0) {
                int worst = h.top();
                h.pop();
                sum -= worst;
                ans++;
            }
        }
        return ans;
    }
};
