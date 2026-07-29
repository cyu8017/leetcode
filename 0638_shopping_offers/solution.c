// LeetCode 0638 - Shopping Offers
// https://leetcode.com/problems/shopping-offers/

#include <limits.h>
#include <stdlib.h>
#include <string.h>

static int encode(const int* needs, int n) {
    int key = 0;
    for (int i = 0; i < n; i++) {
        key = key * 7 + needs[i];
    }
    return key;
}

static int dfs(int* price, int priceSize, int** special, int specialSize, int* specialColSize,
               int* needs, int* memo, int memoSize) {
    int key = encode(needs, priceSize);
    if (key < memoSize && memo[key] >= 0) {
        return memo[key];
    }
    int cost = 0;
    for (int i = 0; i < priceSize; i++) {
        cost += needs[i] * price[i];
    }
    for (int s = 0; s < specialSize; s++) {
        int valid = 1;
        int nxt[6];
        for (int i = 0; i < priceSize; i++) {
            if (needs[i] < special[s][i]) {
                valid = 0;
                break;
            }
            nxt[i] = needs[i] - special[s][i];
        }
        if (!valid) {
            continue;
        }
        int offerCost = special[s][specialColSize[s] - 1] +
                        dfs(price, priceSize, special, specialSize, specialColSize, nxt, memo, memoSize);
        if (offerCost < cost) {
            cost = offerCost;
        }
    }
    if (key < memoSize) {
        memo[key] = cost;
    }
    return cost;
}

int shoppingOffers(int* price, int priceSize, int** special, int specialSize, int* specialColSize,
                   int* needs, int needsSize) {
    (void)needsSize;
    int memoSize = 1;
    for (int i = 0; i < priceSize; i++) {
        memoSize *= 7;
    }
    int* memo = (int*)malloc((size_t)memoSize * sizeof(int));
    for (int i = 0; i < memoSize; i++) {
        memo[i] = -1;
    }
    int answer = dfs(price, priceSize, special, specialSize, specialColSize, needs, memo, memoSize);
    free(memo);
    return answer;
}
