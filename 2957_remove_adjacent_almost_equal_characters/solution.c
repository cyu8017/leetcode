// LeetCode 2957 - Remove Adjacent Almost-Equal Characters
// https://leetcode.com/problems/remove-adjacent-almost-equal-characters/

#include <string.h>

int removeAlmostEqualCharacters(char* word) {
    int ans = 0, n = (int)strlen(word), i = 1;
    while (i < n) {
        int d = (int)word[i] - (int)word[i - 1];
        if (d < 0) d = -d;
        if (d <= 1) { ans++; i += 2; }
        else i++;
    }
    return ans;
}
