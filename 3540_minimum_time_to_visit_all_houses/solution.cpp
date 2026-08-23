// LeetCode 3540 - Minimum Time to Visit All Houses
// https://leetcode.com/problems/minimum-time-to-visit-all-houses/

#include <vector>
#include <algorithm>

class Solution {
public:
    long long minTotalTime(std::vector<int>& forward, std::vector<int>& backward, std::vector<int>& queries) {
        int n = (int)forward.size();
        int sumB = 0;
        for (int v : backward) sumB += v;
        std::vector<int> pf(n + 1), pb(n + 1);
        for (int i = 0; i < n; i++) {
            pf[i + 1] = pf[i] + forward[i];
            pb[i + 1] = pb[i] + backward[i];
        }
        long long ans = 0;
        int pos = 0;
        for (int q : queries) {
            int r = 0;
            if (q < pos) r = pf[n];
            r += pf[q] - pf[pos];
            int l = 0;
            if (q > pos) l = sumB;
            l += pb[pos] - pb[q];
            ans += std::min(l, r);
            pos = q;
        }
        return ans;
    }
};
