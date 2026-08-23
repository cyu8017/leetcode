// LeetCode 3168 - Minimum Number of Chairs in a Waiting Room
// https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/

#include <string>

class Solution {
public:
    int minimumChairs(std::string s) {
        int cnt = 0, left = 0;
        for (char c : s) {
            if (c == 'E') {
                if (left > 0) left--;
                else cnt++;
            } else left++;
        }
        return cnt;
    }
};
