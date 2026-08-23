// LeetCode 3964 - Minimum Lights To Illuminate A Road
// https://leetcode.com/problems/minimum-lights-to-illuminate-a-road/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minLights(std::vector<int>& lights) {
        int n = (int)lights.size();
        std::vector<int> d(n, 0);
        for (int i = 0; i < n; i++) {
            int v = lights[i];
            if (v > 0) {
                int l = std::max(0, i - v);
                int r = std::min(n - 1, i + v);
                d[l]++;
                if (r + 1 < n) d[r + 1]--;
            }
        }
        int s = 0, cnt = 0, ans = 0;
        for (int x : d) {
            s += x;
            if (s == 0) cnt++;
            else {
                ans += (cnt + 2) / 3;
                cnt = 0;
            }
        }
        ans += (cnt + 2) / 3;
        return ans;
    }
};
