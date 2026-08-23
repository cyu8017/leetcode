// LeetCode 2800 - Shortest String That Contains Three Strings
// https://leetcode.com/problems/shortest-string-that-contains-three-strings/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::string minimumString(std::string a, std::string b, std::string c) {
        auto merge = [](const std::string& x, const std::string& y) {
            if (x.find(y) != std::string::npos) return x;
            std::string best = x + y;
            int n = std::min((int)x.size(), (int)y.size());
            for (int i = n; i > 0; i--) {
                if (x.substr(x.size() - i) == y.substr(0, i)) {
                    std::string cand = x + y.substr(i);
                    if (cand.size() < best.size() || (cand.size() == best.size() && cand < best)) best = cand;
                    break;
                }
            }
            return best;
        };
        std::vector<std::vector<std::string>> perms = {
            {a, b, c}, {a, c, b}, {b, a, c}, {b, c, a}, {c, a, b}, {c, b, a}
        };
        std::string ans;
        for (auto& p : perms) {
            std::string cur = merge(merge(p[0], p[1]), p[2]);
            if (ans.empty() || cur.size() < ans.size() || (cur.size() == ans.size() && cur < ans)) ans = cur;
        }
        return ans;
    }
};
