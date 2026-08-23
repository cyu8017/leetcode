// LeetCode 3163 - String Compression III
// https://leetcode.com/problems/string-compression-iii/

#include <string>
#include <algorithm>

class Solution {
public:
    std::string compressedString(std::string word) {
        std::string ans;
        int n = (int)word.size();
        for (int i = 0; i < n; ) {
            int j = i + 1;
            while (j < n && word[j] == word[i]) j++;
            int k = j - i;
            while (k > 0) {
                int x = std::min(9, k);
                ans.push_back(char('0' + x));
                ans.push_back(word[i]);
                k -= x;
            }
            i = j;
        }
        return ans;
    }
};
