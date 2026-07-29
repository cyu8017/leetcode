// LeetCode 0925 - Long Pressed Name
// https://leetcode.com/problems/long-pressed-name/

#include <string>

class Solution {
public:
    bool isLongPressedName(std::string name, std::string typed) {
        int i = 0, j = 0;
        while (j < (int)typed.size()) {
            if (i < (int)name.size() && name[i] == typed[j]) {
                i++;
                j++;
            } else if (j > 0 && typed[j] == typed[j - 1]) {
                j++;
            } else {
                return false;
            }
        }
        return i == (int)name.size();
    }
};
