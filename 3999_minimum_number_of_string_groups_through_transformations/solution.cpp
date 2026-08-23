// LeetCode 3999 - Minimum Number of String Groups Through Transformations
// https://leetcode.com/problems/minimum-number-of-string-groups-through-transformations/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
    static int leastRotation(const std::string& s) {
        int n = (int)s.size();
        int i = 0, j = 1, k = 0;
        while (i < n && j < n && k < n) {
            char a = s[(i + k) % n];
            char b = s[(j + k) % n];
            if (a == b) ++k;
            else {
                if (a > b) i += k + 1;
                else j += k + 1;
                if (i == j) ++j;
                k = 0;
            }
        }
        return i < j ? i : j;
    }

    static std::string canonicalRotate(std::string s) {
        int n = (int)s.size();
        if (n <= 1) return s;
        int r = leastRotation(s);
        if (r == 0) return s;
        return s.substr(r) + s.substr(0, r);
    }

public:
    int minimumGroups(std::vector<std::string>& words) {
        std::vector<std::string> keys;
        keys.reserve(words.size());
        for (const std::string& w : words) {
            int n = (int)w.size();
            std::string even, odd;
            for (int i = 0; i < n; i++) {
                if (i % 2 == 0) even.push_back(w[i]);
                else odd.push_back(w[i]);
            }
            even = canonicalRotate(even);
            odd = canonicalRotate(odd);
            keys.push_back(even + "#" + odd);
        }
        std::sort(keys.begin(), keys.end());
        int groups = 0;
        for (int i = 0; i < (int)keys.size(); i++) {
            if (i == 0 || keys[i] != keys[i - 1]) ++groups;
        }
        return groups;
    }
};
