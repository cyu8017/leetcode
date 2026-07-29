// LeetCode 1333 - Filter Restaurants by Vegan-Friendly, Price and Distance
// https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/

#include <stdlib.h>

typedef struct { int id, rating; } Rest;

static int cmp_rest(const void* a, const void* b) {
    const Rest* x = (const Rest*)a;
    const Rest* y = (const Rest*)b;
    if (x->rating != y->rating) return y->rating - x->rating;
    return y->id - x->id;
}

int* filterRestaurants(int** restaurants, int restaurantsSize, int* restaurantsColSize,
                       int veganFriendly, int maxPrice, int maxDistance, int* returnSize) {
    (void)restaurantsColSize;
    Rest* valid = (Rest*)malloc(restaurantsSize * sizeof(Rest));
    int vn = 0;
    for (int i = 0; i < restaurantsSize; i++) {
        int* row = restaurants[i];
        if ((!veganFriendly || row[2]) && row[3] <= maxPrice && row[4] <= maxDistance) {
            valid[vn].id = row[0];
            valid[vn].rating = row[1];
            vn++;
        }
    }
    qsort(valid, vn, sizeof(Rest), cmp_rest);
    int* ans = (int*)malloc(vn * sizeof(int));
    for (int i = 0; i < vn; i++) ans[i] = valid[i].id;
    free(valid);
    *returnSize = vn;
    return ans;
}
