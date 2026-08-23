// LeetCode 2957 - Remove Adjacent Almost-Equal Characters
// https://leetcode.com/problems/remove-adjacent-almost-equal-characters/

#include <cstdlib>
#include <string>

class Solution {
public:
    int removeAlmostEqualCharacters(std::string word) {
        int ans = 0, n = (int)word.size(), i = 1;
        while (i < n) {
            if (std::abs((int)word[i] - (int)word[i - 1]) <= 1) {
                ans++;
                i += 2;
            } else i++;
        }
        return ans;
    }
};
