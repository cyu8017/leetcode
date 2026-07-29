// LeetCode 0925 - Long Pressed Name
// https://leetcode.com/problems/long-pressed-name/

#include <stdbool.h>

bool isLongPressedName(char* name, char* typed) {
    int i = 0;
    for (int j = 0; typed[j]; j++) {
        if (name[i] && name[i] == typed[j]) i++;
        else if (j == 0 || typed[j] != typed[j - 1]) return false;
    }
    return name[i] == 0;
}
