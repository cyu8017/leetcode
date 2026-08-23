// LeetCode 2896 - Apply Operations to Make Two Strings Equal
// https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/

#include <string>
#include <vector>

class Solution {
public:
    int minOperations(std::string s1, std::string s2, int x) {
        std::vector<int> diff;
        for (int i = 0; i < (int)s1.size(); i++)
            if (s1[i] != s2[i]) diff.push_back(i);
        int m = (int)diff.size();
        if (m % 2 == 1) return -1;
        if (m == 0) return 0;
        std::vector<int> dp2(m + 1, 1 << 30);
        dp2[0] = 0;
        for (int i = 0; i < m; i++) {
            if (dp2[i] >= (1 << 30)) continue;
            if (i + 1 < m) {
                int cand = diff[i + 1] - diff[i];
                if (cand > x) cand = x;
                if (dp2[i] + cand < dp2[i + 2]) dp2[i + 2] = dp2[i] + cand;
            }
        }
        return dp2[m] >= (1 << 30) ? -1 : dp2[m];
    }
};
