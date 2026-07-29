// LeetCode 0777 - Swap Adjacent in LR String
// https://leetcode.com/problems/swap-adjacent-in-lr-string/

#include <stdbool.h>
#include <string.h>

bool canTransform(char* start, char* end) {
    int n = (int)strlen(start);
    int i = 0, j = 0;
    while (1) {
        while (i < n && start[i] == 'X') i++;
        while (j < n && end[j] == 'X') j++;
        if (i == n && j == n) return true;
        if (i == n || j == n || start[i] != end[j]) return false;
        if (start[i] == 'L' && i < j) return false;
        if (start[i] == 'R' && i > j) return false;
        i++;
        j++;
    }
}
