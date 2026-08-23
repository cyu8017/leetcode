// LeetCode 3557 - Find Maximum Number of Non Intersecting Substrings
// https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/

#include <string>
#include <unordered_map>

class Solution {
public:
    int maxSubstrings(std::string word) {
        int ans = 0;
        std::unordered_map<char, int> first;
        for (int i = 0; i < (int)word.size(); i++) {
            char c = word[i];
            if (!first.count(c)) first[c] = i;
            else if (i - first[c] + 1 >= 4) {
                ans++;
                first.clear();
            }
        }
        return ans;
    }
};
