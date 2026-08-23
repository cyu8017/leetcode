// LeetCode 3114 - Latest Time You Can Obtain After Replacing Characters
// https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/

#include <cstdio>
#include <string>

class Solution {
public:
    std::string findLatestTime(std::string s) {
        for (int h = 11; ; h--) {
            for (int m = 59; m >= 0; m--) {
                char t[6];
                std::snprintf(t, sizeof(t), "%02d:%02d", h, m);
                bool ok = true;
                for (int i = 0; i < 5; i++) {
                    if (s[i] != '?' && s[i] != t[i]) {
                        ok = false;
                        break;
                    }
                }
                if (ok) return std::string(t);
            }
        }
    }
};
