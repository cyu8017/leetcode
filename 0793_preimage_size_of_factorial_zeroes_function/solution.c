// LeetCode 0793 - Preimage Size of Factorial Zeroes Function
static long long zeros(long long x) {
    long long count = 0;
    while (x) { x /= 5; count += x; }
    return count;
}

static long long firstGe(long long target) {
    long long lo = 0, hi = 5 * (target + 1);
    while (lo < hi) {
        long long mid = (lo + hi) / 2;
        if (zeros(mid) < target) lo = mid + 1; else hi = mid;
    }
    return lo;
}

int preimageSizeFZF(int k) {
    return zeros(firstGe(k)) == k ? 5 : 0;
}
