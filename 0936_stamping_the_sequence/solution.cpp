// LeetCode 0936 - Stamping The Sequence
// https://leetcode.com/problems/stamping-the-sequence/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> movesToStamp(std::string stamp, std::string target) {
        int n = (int)target.size(), m = (int)stamp.size();
        std::vector<char> done(n, 0);
        std::vector<int> ans;
        bool changed = true;
        while (changed) {
            changed = false;
            for (int i = n - m; i >= 0; i--) {
                bool ok = true, any = false;
                for (int j = 0; j < m; j++) {
                    if (!done[i + j] && target[i + j] != stamp[j]) { ok = false; break; }
                    if (!done[i + j]) any = true;
                }
                if (ok && any) {
                    for (int j = 0; j < m; j++) done[i + j] = 1;
                    ans.push_back(i);
                    changed = true;
                    break;
                }
            }
        }
        for (char d : done) if (!d) return {};
        std::reverse(ans.begin(), ans.end());
        return ans;
    }
};
