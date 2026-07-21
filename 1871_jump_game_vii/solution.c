// LeetCode 1871 - Jump Game VII
// https://leetcode.com/problems/jump-game-vii/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool canReach(char* s, int minJump, int maxJump) {
    int n = (int)strlen(s);
    int* reachable = (int*)calloc((size_t)n, sizeof(int));
    int* prefix = (int*)calloc((size_t)(n + 1), sizeof(int));
    reachable[0] = 1;
    for (int i = 0; i < n; i++) {
        if (i > 0 && s[i] == '0') {
            int left = i - maxJump;
            if (left < 0) left = 0;
            int right = i - minJump;
            if (right >= left && prefix[right + 1] - prefix[left] > 0) reachable[i] = 1;
        }
        prefix[i + 1] = prefix[i] + reachable[i];
    }
    bool ok = reachable[n - 1] != 0;
    free(reachable);
    free(prefix);
    return ok;
}
