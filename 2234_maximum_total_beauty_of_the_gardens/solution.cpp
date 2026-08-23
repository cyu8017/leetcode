// LeetCode 2234 - Maximum Total Beauty of the Gardens
// https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/

#include <vector>
#include <algorithm>

class Solution {
public:
    long long maximumBeauty(std::vector<int>& flowers, long long newFlowers, int target, int full, int partial) {
        int n = (int)flowers.size();
        for (int& f : flowers) if (f > target) f = target;
        std::sort(flowers.begin(), flowers.end());
        long long sum = 0;
        for (int f : flowers) sum += f;
        if (1LL * target * n - sum <= newFlowers) return 1LL * n * full;
        std::vector<long long> pref(n + 1);
        for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] + flowers[i];
        long long ans = 0;
        int j = n - 1;
        long long remain = newFlowers;
        for (int complete = 0; complete <= n; ++complete) {
            if (complete > 0) {
                long long need = target - flowers[n - complete];
                if (remain < need) break;
                remain -= need;
            }
            while (j >= n - complete || (j >= 0 && 1LL * flowers[j] * (j + 1) - pref[j + 1] > remain)) j--;
            long long partialVal = 0;
            if (j >= 0) {
                long long extra = (remain - (1LL * flowers[j] * (j + 1) - pref[j + 1])) / (j + 1);
                partialVal = flowers[j] + extra;
                if (partialVal >= target) partialVal = target - 1;
            }
            ans = std::max(ans, 1LL * complete * full + partialVal * partial);
        }
        return ans;
    }
};
