// LeetCode 1963 - Minimum Number of Swaps to Make the String Balanced
#include <algorithm>
#include <string>

class Solution {
public:
    int minSwaps(std::string s) {
        int bal = 0, mx = 0;
        for (char ch : s) {
            if (ch == '[') bal++;
            else bal--;
            mx = std::min(mx, bal);
        }
        return (-mx + 1) / 2;
    }
};
