// LeetCode 3014 - Minimum Number of Pushes to Type Word I
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

#include <string.h>

int minimumPushes(char* word) {
    int n = (int)strlen(word);
    int ans = 0, k = 1;
    for (int i = 0; i < n / 8; i++) {
        ans += k * 8;
        k++;
    }
    ans += k * (n % 8);
    return ans;
}
