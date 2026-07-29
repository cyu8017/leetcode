// LeetCode 1156 - Swap For Longest Repeated Character Substring
// https://leetcode.com/problems/swap-for-longest-repeated-character-substring/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int maxRepOpt1(std::string text) {
        std::vector<int> count(26, 0);
        for (char ch : text) ++count[ch - 'a'];
        int n = static_cast<int>(text.size()), ans = 0, i = 0;
        while (i < n) {
            int j = i;
            while (j < n && text[j] == text[i]) ++j;
            int length = j - i;
            int k = j + 1;
            while (k < n && text[k] == text[i]) ++k;
            int length2 = j < n ? k - j - 1 : 0;
            ans = std::max(ans, std::min(length + length2 + 1, count[text[i] - 'a']));
            i = j;
        }
        return ans;
    }
};
