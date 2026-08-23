// LeetCode 3076 - Shortest Uncommon Substring in an Array
// https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> shortestSubstrings(std::vector<std::string>& arr) {
        int n = (int)arr.size();
        std::vector<std::string> ans(n);
        for (int i = 0; i < n; i++) {
            const auto& s = arr[i];
            int m = (int)s.size();
            for (int j = 1; j <= m && ans[i].empty(); j++) {
                for (int l = 0; l <= m - j; l++) {
                    std::string sub = s.substr(l, j);
                    if (ans[i].empty() || ans[i] > sub) {
                        bool ok = true;
                        for (int k = 0; k < n; k++) {
                            if (k != i && arr[k].find(sub) != std::string::npos) {
                                ok = false;
                                break;
                            }
                        }
                        if (ok) ans[i] = sub;
                    }
                }
            }
        }
        return ans;
    }
};
