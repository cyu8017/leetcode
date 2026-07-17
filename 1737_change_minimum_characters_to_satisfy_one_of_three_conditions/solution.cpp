// LeetCode 1737 - Change Minimum Characters to Satisfy One of Three Conditions
// https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int minCharacters(std::string a, std::string b) {
        std::vector<int> ca(26, 0), cb(26, 0);
        for (char ch : a) {
            ca[ch - 'a']++;
        }
        for (char ch : b) {
            cb[ch - 'a']++;
        }
        int n = a.size();
        int m = b.size();
        int maxCount = 0;
        for (int i = 0; i < 26; i++) {
            maxCount = std::max(maxCount, std::max(ca[i], cb[i]));
        }
        int ans = n + m - maxCount;
        int preA = 0, preB = 0;
        for (int code = 0; code < 25; code++) {
            preA += ca[code];
            preB += cb[code];
            ans = std::min({ans, n - preA + preB, m - preB + preA});
        }
        return ans;
    }
};
