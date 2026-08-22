// LeetCode 1540 - Can Convert String in K Moves
// https://leetcode.com/problems/can-convert-string-in-k-moves/

#include <string.h>
#include <stdbool.h>

bool canConvertString(char* s, char* t, int k) {
    int n = (int)strlen(s);
    if (n != (int)strlen(t)) return false;
    int used[26] = {0};
    for (int i = 0; i < n; i++) {
        int shift = (t[i] - s[i] + 26) % 26;
        if (shift) {
            used[shift]++;
            if (shift + 26 * (used[shift] - 1) > k) return false;
        }
    }
    return true;
}
