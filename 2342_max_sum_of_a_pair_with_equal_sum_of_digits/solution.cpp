// LeetCode 2342 - Max Sum of a Pair With Equal Sum of Digits
// https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int maximumSum(std::vector<int>& nums) {
        auto digitSum = [](int x) {
            int s = 0;
            while (x > 0) {
                s += x % 10;
                x /= 10;
            }
            return s;
        };
        std::unordered_map<int, int> best;
        int ans = -1;
        for (int x : nums) {
            int ds = digitSum(x);
            auto it = best.find(ds);
            if (it != best.end()) {
                if (it->second + x > ans) ans = it->second + x;
                if (x > it->second) it->second = x;
            } else {
                best[ds] = x;
            }
        }
        return ans;
    }
};
