// LeetCode 3090 - Maximum Length Substring With Two Occurrences
// https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

#include <algorithm>
#include <string>

class Solution {
public:
    int maximumLengthSubstring(std::string s) {
        int l = 0, ans = 0, cnt[26] = {};
        for (int r = 0; r < (int)s.size(); r++) {
            int idx = s[r] - 'a';
            cnt[idx]++;
            while (cnt[idx] > 2) {
                cnt[s[l] - 'a']--;
                l++;
            }
            ans = std::max(ans, r - l + 1);
        }
        return ans;
    }
};
