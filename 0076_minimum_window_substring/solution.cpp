// LeetCode 0076 - Minimum Window Substring
// https://leetcode.com/problems/minimum-window-substring/

#include <limits>
#include <string>
#include <unordered_map>

class Solution {
public:
    std::string minWindow(std::string s, std::string t) {
        if (t.empty()) {
            return "";
        }

        std::unordered_map<char, int> need;
        for (char ch : t) {
            need[ch]++;
        }

        int required = static_cast<int>(need.size());
        int formed = 0;
        std::unordered_map<char, int> window;
        int left = 0;
        int bestLen = std::numeric_limits<int>::max();
        int bestLeft = 0;

        for (int right = 0; right < static_cast<int>(s.size()); right++) {
            char ch = s[right];
            window[ch]++;
            if (need.count(ch) && window[ch] == need[ch]) {
                formed++;
            }

            while (formed == required) {
                if (right - left + 1 < bestLen) {
                    bestLen = right - left + 1;
                    bestLeft = left;
                }

                char leftCh = s[left];
                window[leftCh]--;
                if (need.count(leftCh) && window[leftCh] < need[leftCh]) {
                    formed--;
                }
                left++;
            }
        }

        if (bestLen == std::numeric_limits<int>::max()) {
            return "";
        }

        return s.substr(bestLeft, bestLen);
    }
};
