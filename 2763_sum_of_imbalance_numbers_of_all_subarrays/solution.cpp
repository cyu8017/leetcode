// LeetCode 2763 - Sum of Imbalance Numbers of All Subarrays
// https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/

#include <set>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int sumImbalanceNumbers(std::vector<int>& nums) {
        int n = (int)nums.size(), ans = 0;
        for (int i = 0; i < n; i++) {
            std::unordered_set<int> seen;
            std::set<int> sortedVals;
            int imbalance = 0;
            for (int j = i; j < n; j++) {
                int x = nums[j];
                if (!seen.count(x)) {
                    seen.insert(x);
                    auto it = sortedVals.lower_bound(x);
                    if (it != sortedVals.begin()) {
                        auto pit = std::prev(it);
                        if (x - *pit != 1) imbalance++;
                    }
                    if (it != sortedVals.end()) {
                        if (*it - x != 1) imbalance++;
                    }
                    if (it != sortedVals.begin() && it != sortedVals.end()) {
                        auto pit = std::prev(it);
                        if (*it - *pit > 1) imbalance--;
                    }
                    sortedVals.insert(x);
                }
                ans += imbalance;
            }
        }
        return ans;
    }
};
