// LeetCode 3494 - Find the Minimum Amount of Time to Brew Potions
// https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/

#include <stdlib.h>

long long minTime(int* skill, int skillSize, int* mana, int manaSize) {
    int n = skillSize, m = manaSize;
    long long* done = (long long*)calloc((size_t)n, sizeof(long long));
    for (int j = 0; j < m; j++) {
        long long t = 0;
        for (int i = 0; i < n; i++) {
            if (done[i] > t) t = done[i];
            t += (long long)skill[i] * mana[j];
            done[i] = t;
        }
        for (int i = n - 2; i >= 0; i--) {
            done[i] = done[i + 1] - (long long)skill[i + 1] * mana[j];
        }
    }
    long long ans = done[n - 1];
    free(done);
    return ans;
}
