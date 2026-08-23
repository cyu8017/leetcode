// LeetCode 3014 - Minimum Number of Pushes to Type Word I
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

#include <string>

class Solution {
public:
    int minimumPushes(std::string word) {
        int n = (int)word.size(), ans = 0, k = 1;
        for (int i = 0; i < n / 8; i++) {
            ans += k * 8;
            k++;
        }
        ans += k * (n % 8);
        return ans;
    }
};
