// LeetCode 2027 - Minimum Moves to Convert String
// https://leetcode.com/problems/minimum-moves-to-convert-string/

#include <string.h>

int minimumMoves(char* s) {
    int ans = 0;
    for (int i = 0; s[i];) {
        if (s[i] == 'X') { ans++; i += 3; }
        else i++;
    }
    return ans;
}
