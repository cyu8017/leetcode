// LeetCode 4005 - Minimum Operations to Make Array Equal III
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-iii/

#include <algorithm>
#include <climits>
#include <numeric>
#include <set>
#include <vector>

class Solution {
    static int cost(int x, int t) {
        if (x == t) return 0;
        if (x % t == 0 || t % x == 0) return 1;
        return 2;
    }

public:
    int minOperations(std::vector<int>& nums) {
        int n = (int)nums.size();
        if (n <= 1) return 0;

        int g = nums[0], mn = nums[0];
        for (int i = 1; i < n; i++) {
            g = std::gcd(g, nums[i]);
            mn = std::min(mn, nums[i]);
        }

        std::set<int> cands;
        for (int x : nums) cands.insert(x);
        for (int d = 1; (long long)d * d <= mn; d++) {
            if (mn % d == 0) {
                cands.insert(d);
                cands.insert(mn / d);
            }
        }
        cands.insert(g);

        int ans = INT_MAX;
        for (int t : cands) {
            int sum = 0;
            for (int x : nums) {
                sum += cost(x, t);
                if (sum >= ans) break;
            }
            ans = std::min(ans, sum);
        }
        return ans;
    }
};
