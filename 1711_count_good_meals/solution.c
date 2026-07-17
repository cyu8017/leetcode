// LeetCode 1711 - Count Good Meals
// https://leetcode.com/problems/count-good-meals/

#include <stdlib.h>
#include <string.h>

#define MAX_VALUE (1 << 20)

int countPairs(int* deliciousness, int deliciousnessSize) {
    const long long mod = 1000000007LL;
    int* seen = (int*)calloc(MAX_VALUE + 1, sizeof(int));
    long long ans = 0;
    for (int i = 0; i < deliciousnessSize; i++) {
        int value = deliciousness[i];
        for (int power = 0; power < 22; power++) {
            long long target = (1LL << power) - value;
            if (target >= 0 && target <= MAX_VALUE) {
                ans += seen[target];
            }
        }
        seen[value]++;
    }
    free(seen);
    return (int)(ans % mod);
}
