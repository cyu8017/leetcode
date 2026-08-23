// LeetCode 3682 - Minimum Index Sum of Common Elements
// https://leetcode.com/problems/minimum-index-sum-of-common-elements/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int minimumSum(std::vector<int>& nums1, std::vector<int>& nums2) {
        const int inf = 1 << 30;
        std::unordered_map<int, int> d;
        for (int i = 0; i < (int)nums2.size(); i++) {
            if (!d.count(nums2[i])) d[nums2[i]] = i;
        }
        int ans = inf;
        for (int i = 0; i < (int)nums1.size(); i++) {
            auto it = d.find(nums1[i]);
            if (it != d.end()) ans = std::min(ans, i + it->second);
        }
        return ans == inf ? -1 : ans;
    }
};
