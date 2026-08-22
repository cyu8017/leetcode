// LeetCode 2315 - Count Asterisks
// https://leetcode.com/problems/count-asterisks/

#include <stdbool.h>
#include <string.h>

int countAsterisks(char* s) {
    int ans = 0;
    bool inside = false;
    for (int i = 0; s[i]; i++) {
        if (s[i] == '|') {
            inside = !inside;
        } else if (s[i] == '*' && !inside) {
            ans++;
        }
    }
    return ans;
}
