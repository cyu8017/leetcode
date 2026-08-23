// LeetCode 3748 - Count Stable Subarrays
// https://leetcode.com/problems/count-stable-subarrays/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<long long> countStableSubarrays(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        int n = (int)nums.size();
        std::vector<int> seg;
        std::vector<long long> s{0};
        int l = 0;
        for (int r = 0; r < n; r++) {
            if (r == n - 1 || nums[r] > nums[r + 1]) {
                seg.push_back(l);
                long long k = r - l + 1;
                s.push_back(s.back() + k * (k + 1) / 2);
                l = r + 1;
            }
        }
        std::vector<long long> ans(queries.size());
        for (int idx = 0; idx < (int)queries.size(); idx++) {
            int left = queries[idx][0], right = queries[idx][1];
            int i = (int)(std::lower_bound(seg.begin(), seg.end(), left + 1) - seg.begin());
            int j = (int)(std::lower_bound(seg.begin(), seg.end(), right + 1) - seg.begin()) - 1;
            if (i > j) {
                long long k = right - left + 1;
                ans[idx] = k * (k + 1) / 2;
            } else {
                long long a = seg[i] - left;
                long long b = right - seg[j] + 1;
                ans[idx] = a * (a + 1) / 2 + s[j] - s[i] + b * (b + 1) / 2;
            }
        }
        return ans;
    }
};
