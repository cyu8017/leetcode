// LeetCode 1601 - Maximum Number of Achievable Transfer Requests
// https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

#include <vector>

class Solution {
public:
    int maximumRequests(int n, std::vector<std::vector<int>>& requests) {
        int ans = 0;
        const int m = static_cast<int>(requests.size());
        for (int mask = 0; mask < (1 << m); ++mask) {
            const int bits = __builtin_popcount(mask);
            if (bits <= ans) {
                continue;
            }
            std::vector<int> bal(n, 0);
            for (int i = 0; i < m; ++i) {
                if (mask >> i & 1) {
                    --bal[requests[i][0]];
                    ++bal[requests[i][1]];
                }
            }
            bool ok = true;
            for (int x : bal) {
                if (x != 0) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                ans = bits;
            }
        }
        return ans;
    }
};
