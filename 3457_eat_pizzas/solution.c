// LeetCode 3457 - Eat Pizzas!
// https://leetcode.com/problems/eat-pizzas/

#include <stdlib.h>

static int cmp_int_asc(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

long long maxWeight(int* pizzas, int pizzasSize) {
    qsort(pizzas, (size_t)pizzasSize, sizeof(int), cmp_int_asc);
    int n = pizzasSize;
    int days = n / 4;
    long long ans = 0;
    int oddDays = (days + 1) / 2;
    int evenDays = days / 2;
    int idx = n - 1;
    for (int i = 0; i < oddDays; i++) {
        ans += pizzas[idx];
        idx--;
    }
    for (int i = 0; i < evenDays; i++) {
        idx--;
        ans += pizzas[idx];
        idx--;
    }
    return ans;
}
