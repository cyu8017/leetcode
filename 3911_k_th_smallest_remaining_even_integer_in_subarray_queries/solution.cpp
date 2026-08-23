// LeetCode 3911 - K-th Smallest Remaining Even Integer in Subarray Queries
// https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<long long> kthSmallestEven(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        int n = (int)nums.size();
        std::vector<int> evenPrefix(n + 1, 0);
        for (int i = 0; i < n; i++) {
            evenPrefix[i + 1] = evenPrefix[i] + (nums[i] % 2 == 0);
        }
        std::vector<long long> ans(queries.size());
        for (int qi = 0; qi < (int)queries.size(); qi++) {
            int l = queries[qi][0], r = queries[qi][1];
            long long k = queries[qi][2];
            long long lo = 1, hi = k + (r - l + 1);
            while (lo < hi) {
                long long mid = (lo + hi) / 2;
                int pos = (int)(std::upper_bound(nums.begin(), nums.end(), 2 * mid) - nums.begin());
                if (pos > r + 1) pos = r + 1;
                int removed = 0;
                if (pos > l) removed = evenPrefix[pos] - evenPrefix[l];
                if (mid - removed >= k) hi = mid;
                else lo = mid + 1;
            }
            ans[qi] = 2 * lo;
        }
        return ans;
    }
};
