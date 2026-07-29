// LeetCode 1100 - Find K-Length Substrings With No Repeated Characters
// https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/

#include <string>
#include <unordered_map>

class Solution {
public:
    int numKLenSubstrNoRepeats(std::string s, int k) {
        if (k > static_cast<int>(s.size())) {
            return 0;
        }
        std::unordered_map<char, int> window;
        for (int i = 0; i < k; ++i) {
            ++window[s[i]];
        }
        int ans = static_cast<int>(window.size()) == k ? 1 : 0;
        for (int i = k; i < static_cast<int>(s.size()); ++i) {
            ++window[s[i]];
            char left = s[i - k];
            if (--window[left] == 0) {
                window.erase(left);
            }
            if (static_cast<int>(window.size()) == k) {
                ++ans;
            }
        }
        return ans;
    }
};
