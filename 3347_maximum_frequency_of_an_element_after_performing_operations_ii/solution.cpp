// LeetCode 3347 - Maximum Frequency of an Element After Performing Operations II
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/

#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int maxFrequency(std::vector<int>& nums, int k, int numOperations) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        std::unordered_map<int, int> freq;
        for (int x : nums) freq[x]++;
        int ans = 1;
        std::vector<int> candidates;
        std::unordered_set<int> seen;
        for (int x : nums) {
            for (int t : {x - k, x, x + k}) {
                if (!seen.count(t)) {
                    seen.insert(t);
                    candidates.push_back(t);
                }
            }
        }
        for (int t : candidates) {
            int lo = (int)(std::lower_bound(nums.begin(), nums.end(), t - k) - nums.begin());
            int hi = (int)(std::upper_bound(nums.begin(), nums.end(), t + k) - nums.begin());
            int can = hi - lo;
            int f = freq.count(t) ? freq[t] : 0;
            int use = can;
            if (use > f + numOperations) use = f + numOperations;
            if (use > ans) ans = use;
        }
        return ans;
    }
};
