// LeetCode 3583 - Count Special Triplets
// https://leetcode.com/problems/count-special-triplets/

#include <stdlib.h>

int specialTriplets(int* nums, int numsSize) {
    /* map via open addressing for values; constraints typically moderate */
    typedef struct { int key; int val; int used; } Ent;
    int cap = 4096;
    Ent* left = (Ent*)calloc((size_t)cap, sizeof(Ent));
    Ent* right = (Ent*)calloc((size_t)cap, sizeof(Ent));
    #define HGET(tab, k, out) do { unsigned h=((unsigned)(k)*2654435761u)%(unsigned)cap; \
        while(tab[h].used && tab[h].key!=(k)) h=(h+1)%(unsigned)cap; \
        if(!tab[h].used){tab[h].used=1;tab[h].key=(k);tab[h].val=0;} out=&tab[h].val; } while(0)
    for (int i = 0; i < numsSize; i++) { int* p; HGET(right, nums[i], p); (*p)++; }
    long long ans = 0, mod = 1000000007LL;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        int *rp, *lp, *rp2, *lp2;
        HGET(right, x, rp); (*rp)--;
        HGET(left, x * 2, lp); HGET(right, x * 2, rp2);
        ans = (ans + (long long)(*lp) * (long long)(*rp2) % mod) % mod;
        HGET(left, x, lp2); (*lp2)++;
    }
    free(left); free(right);
    return (int)ans;
}
