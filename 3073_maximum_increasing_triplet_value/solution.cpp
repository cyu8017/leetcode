// LeetCode 3073 - Maximum Increasing Triplet Value
// https://leetcode.com/problems/maximum-increasing-triplet-value/

#include <algorithm>
#include <set>
#include <vector>

class Solution {
public:
    int maximumTripletValue(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> right(n);
        right[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) right[i] = std::max(nums[i], right[i + 1]);
        std::set<int> ts;
        ts.insert(nums[0]);
        int ans = 0;
        for (int j = 1; j < n - 1; j++) {
            if (right[j + 1] > nums[j]) {
                auto it = ts.lower_bound(nums[j]);
                if (it != ts.begin()) {
                    --it;
                    ans = std::max(ans, *it - nums[j] + right[j + 1]);
                }
            }
            ts.insert(nums[j]);
        }
        return ans;
    }
};
