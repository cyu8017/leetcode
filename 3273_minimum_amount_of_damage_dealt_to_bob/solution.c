// LeetCode 3273 - Minimum Amount of Damage Dealt to Bob
// https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/

#include <stdlib.h>

typedef struct { int dmg, hits; } Enemy;

static int cmpE(const void* a, const void* b) {
    const Enemy* x = a, *y = b;
    long long lhs = (long long)x->hits * y->dmg;
    long long rhs = (long long)y->hits * x->dmg;
    return (lhs > rhs) - (lhs < rhs);
}

long long minDamage(int power, int* damage, int damageSize, int* health, int healthSize) {
    (void)healthSize;
    int n = damageSize;
    Enemy* arr = (Enemy*)malloc((size_t)n * sizeof(Enemy));
    long long totalDmg = 0;
    for (int i = 0; i < n; i++) {
        int hits = (health[i] + power - 1) / power;
        arr[i] = (Enemy){damage[i], hits};
        totalDmg += damage[i];
    }
    qsort(arr, (size_t)n, sizeof(Enemy), cmpE);
    long long ans = 0, cur = totalDmg;
    for (int i = 0; i < n; i++) {
        ans += cur * arr[i].hits;
        cur -= arr[i].dmg;
    }
    free(arr);
    return ans;
}
