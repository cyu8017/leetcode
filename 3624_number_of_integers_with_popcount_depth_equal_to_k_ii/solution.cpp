// LeetCode 3624 - Number of Integers With Popcount Depth Equal to K II
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/

#include <vector>

class Solution {
    int depth(long long x) {
        if (x == 1) return 0;
        int d = 0;
        while (x > 1) {
            x = __builtin_popcountll((unsigned long long)x);
            d++;
        }
        return d;
    }

public:
    std::vector<int> popcountDepth(std::vector<long long>& nums, std::vector<std::vector<long long>>& queries) {
        std::vector<long long> a = nums;
        std::vector<int> ans;
        for (auto& q : queries) {
            if (q[0] == 1) {
                int l = (int)q[1], r = (int)q[2], k = (int)q[3], cnt = 0;
                for (int i = l; i <= r; i++)
                    if (depth(a[i]) == k) cnt++;
                ans.push_back(cnt);
            } else {
                a[(int)q[1]] = q[2];
            }
        }
        return ans;
    }
};
