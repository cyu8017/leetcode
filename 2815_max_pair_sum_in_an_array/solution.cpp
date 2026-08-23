// LeetCode 2815 - Max Pair Sum in an Array
// https://leetcode.com/problems/max-pair-sum-in-an-array/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int maxSum(std::vector<int>& nums) {
        std::unordered_map<int, int> best;
        int ans = -1;
        for (int v : nums) {
            int x = v, md = 0;
            while (x > 0) { md = std::max(md, x % 10); x /= 10; }
            if (best.count(md)) {
                ans = std::max(ans, best[md] + v);
                best[md] = std::max(best[md], v);
            } else best[md] = v;
        }
        return ans;
    }
};
