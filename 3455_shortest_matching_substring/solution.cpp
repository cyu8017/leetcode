// LeetCode 3455 - Shortest Matching Substring
// https://leetcode.com/problems/shortest-matching-substring/

#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    int shortestMatchingSubstring(std::string s, std::string p) {
        std::vector<std::string> parts;
        std::string cur;
        for (char c : p) {
            if (c == '*') {
                parts.push_back(cur);
                cur.clear();
            } else cur.push_back(c);
        }
        parts.push_back(cur);
        while ((int)parts.size() < 3) parts.push_back("");
        std::string a = parts[0], b = parts[1], c = parts[2];
        int n = (int)s.size();
        auto findAll = [&](const std::string& sub) {
            std::vector<int> res;
            if (sub.empty()) {
                res.resize(n + 1);
                for (int i = 0; i <= n; i++) res[i] = i;
                return res;
            }
            for (int i = 0; i + (int)sub.size() <= n; i++) {
                if (s.compare(i, sub.size(), sub) == 0) res.push_back(i);
            }
            return res;
        };
        auto sortSearch = [](const std::vector<int>& arr, int x) {
            return (int)(std::lower_bound(arr.begin(), arr.end(), x) - arr.begin());
        };
        auto posA = findAll(a), posB = findAll(b), posC = findAll(c);
        int ans = n + 1;
        for (int ia : posA) {
            int endA = ia + (int)a.size();
            int bi = sortSearch(posB, endA);
            for (; bi < (int)posB.size(); bi++) {
                int endB = posB[bi] + (int)b.size();
                int ci = sortSearch(posC, endB);
                if (ci < (int)posC.size()) {
                    int length = posC[ci] + (int)c.size() - ia;
                    if (length < ans) ans = length;
                }
                if (b.empty()) break;
                break;
            }
        }
        return ans == n + 1 ? -1 : ans;
    }
};
