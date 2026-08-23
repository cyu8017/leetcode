// LeetCode 3356 - Zero Array Transformation II
// https://leetcode.com/problems/zero-array-transformation-ii/

#include <vector>

class Solution {
public:
    int minZeroArray(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        int n = (int)nums.size();
        auto ok = [&](int k) {
            std::vector<long long> diff(n + 1);
            for (int i = 0; i < k; i++) {
                auto& q = queries[i];
                diff[q[0]] += q[2];
                diff[q[1] + 1] -= q[2];
            }
            long long cur = 0;
            for (int i = 0; i < n; i++) {
                cur += diff[i];
                if (cur < nums[i]) return false;
            }
            return true;
        };
        if (ok(0)) return 0;
        int lo = 1, hi = (int)queries.size() + 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (mid <= (int)queries.size() && ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        if (lo > (int)queries.size()) return -1;
        return lo;
    }
};
