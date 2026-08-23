// LeetCode 3569 - Maximize Count of Distinct Primes After Split
// https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> maximumCount(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        int mx = 0;
        for (int v : nums) mx = std::max(mx, v);
        for (auto& q : queries) mx = std::max(mx, q[1]);
        std::vector<bool> isP(mx + 1, false);
        for (int i = 2; i <= mx; i++) isP[i] = true;
        for (int i = 2; i * i <= mx; i++) {
            if (isP[i]) {
                for (int j = i * i; j <= mx; j += i) isP[j] = false;
            }
        }
        std::vector<int> ans(queries.size());
        for (int qi = 0; qi < (int)queries.size(); qi++) {
            nums[queries[qi][0]] = queries[qi][1];
            int best = 0;
            std::unordered_map<int, int> left, right;
            for (int v : nums) {
                if (v <= mx && isP[v]) right[v]++;
            }
            for (int i = 0; i < (int)nums.size() - 1; i++) {
                int v = nums[i];
                if (v <= mx && isP[v]) {
                    left[v]++;
                    if (--right[v] == 0) right.erase(v);
                }
                best = std::max(best, (int)left.size() + (int)right.size());
            }
            ans[qi] = best;
        }
        return ans;
    }
};
