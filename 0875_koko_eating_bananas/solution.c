// LeetCode 0875 - Koko Eating Bananas
// https://leetcode.com/problems/koko-eating-bananas/

static long long hours_needed(int* piles, int n, int k) {
    long long h = 0;
    for (int i = 0; i < n; i++) h += (piles[i] + (long long)k - 1) / k;
    return h;
}

int minEatingSpeed(int* piles, int pilesSize, int h) {
    int lo = 1, hi = 1;
    for (int i = 0; i < pilesSize; i++) if (piles[i] > hi) hi = piles[i];
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (hours_needed(piles, pilesSize, mid) <= h) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
