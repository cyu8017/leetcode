// LeetCode 3304 - Find the K-th Character in String Game I
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

#include <stdlib.h>

char kthCharacter(int k) {
    char* s = (char*)malloc((size_t)(k * 2 + 8));
    int len = 1;
    s[0] = 'a';
    while (len < k) {
        int n = len;
        for (int i = 0; i < n && len < k * 2; i++) {
            s[len++] = (char)('a' + ((s[i] - 'a' + 1) % 26));
        }
    }
    char ans = s[k - 1];
    free(s);
    return ans;
}
