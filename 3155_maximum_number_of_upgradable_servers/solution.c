// LeetCode 3155 - Maximum Number of Upgradable Servers
// https://leetcode.com/problems/maximum-number-of-upgradable-servers/

#include <stdlib.h>

int* maxUpgrades(int* count, int countSize, int* upgrade, int upgradeSize, int* sell, int sellSize, int* money, int moneySize, int* returnSize) {
    (void)upgradeSize; (void)sellSize; (void)moneySize;
    int* ans = malloc(countSize * sizeof(int));
    for (int i = 0; i < countSize; i++) {
        long long v = ((long long)count[i] * sell[i] + money[i]) / (upgrade[i] + sell[i]);
        ans[i] = count[i] < v ? count[i] : (int)v;
    }
    *returnSize = countSize;
    return ans;
}
