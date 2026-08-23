// LeetCode 3722 - Lexicographically Smallest String After Reverse
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/

#include <algorithm>
#include <string>

class Solution {
public:
    std::string lexSmallest(std::string s) {
        std::string ans = s;
        int n = (int)s.size();
        for (int k = 1; k <= n; k++) {
            std::string t1 = s.substr(0, k);
            std::reverse(t1.begin(), t1.end());
            t1 += s.substr(k);
            std::string t2 = s.substr(0, n - k);
            std::string suf = s.substr(n - k);
            std::reverse(suf.begin(), suf.end());
            t2 += suf;
            ans = std::min({ans, t1, t2});
        }
        return ans;
    }
};
