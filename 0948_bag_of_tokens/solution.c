// LeetCode 0948 - Bag of Tokens
// https://leetcode.com/problems/bag-of-tokens/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int bagOfTokensScore(int* tokens, int tokensSize, int power) {
    qsort(tokens, (size_t)tokensSize, sizeof(int), cmpInt);
    int i = 0, j = tokensSize - 1, score = 0, ans = 0;
    while (i <= j) {
        if (power >= tokens[i]) {
            power -= tokens[i++];
            score++;
            if (score > ans) ans = score;
        } else if (score) {
            power += tokens[j--];
            score--;
        } else break;
    }
    return ans;
}
