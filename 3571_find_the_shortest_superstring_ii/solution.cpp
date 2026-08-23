// LeetCode 3571 - Find the Shortest Superstring II
// https://leetcode.com/problems/find-the-shortest-superstring-ii/

#include <string>

class Solution {
public:
    std::string shortestSuperstring(std::string s1, std::string s2) {
        if (s1.size() > s2.size()) return shortestSuperstring(s2, s1);
        int m = (int)s1.size();
        if (s2.find(s1) != std::string::npos) return s2;
        for (int i = 0; i < m; i++) {
            if (s2.rfind(s1.substr(i), 0) == 0) return s1.substr(0, i) + s2;
            if (s2.size() >= (size_t)(m - i) && s2.compare(s2.size() - (m - i), m - i, s1, 0, m - i) == 0)
                return s2 + s1.substr(m - i);
        }
        return s1 + s2;
    }
};
