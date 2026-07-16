// LeetCode 0434 - Number of Segments in a String
// https://leetcode.com/problems/number-of-segments-in-a-string/

#include <string>

class Solution {
public:
    int countSegments(std::string s) {
        int count = 0;
        bool inSegment = false;
        for (char ch : s) {
            if (ch != ' ') {
                if (!inSegment) {
                    ++count;
                    inSegment = true;
                }
            } else {
                inSegment = false;
            }
        }
        return count;
    }
};
