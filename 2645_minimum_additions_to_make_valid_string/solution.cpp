// LeetCode 2645 - Minimum Additions to Make Valid String
// https://leetcode.com/problems/minimum-additions-to-make-valid-string/

#include <string>

class Solution {
public:
    int addMinimum(std::string word) {
        int ans = 0, expect = 0, i = 0, n = (int)word.size();
        while (i < n) {
            char need = 'a' + expect;
            if (word[i] == need) i++;
            else ans++;
            expect = (expect + 1) % 3;
        }
        ans += (3 - expect) % 3;
        return ans;
    }
};
