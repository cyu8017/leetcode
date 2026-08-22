// LeetCode 2226 - Maximum Candies Allocated to K Children
// https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

int maximumCandies(int* candies, int candiesSize, long long k) {
    int mx = 0;
    for (int i = 0; i < candiesSize; i++) if (candies[i] > mx) mx = candies[i];
    int lo = 0, hi = mx;
    while (lo < hi) {
        int mid = (lo + hi + 1) / 2;
        int ok = 1;
        if (mid == 0) ok = 1;
        else {
            long long cnt = 0;
            ok = 0;
            for (int i = 0; i < candiesSize; i++) {
                cnt += candies[i] / mid;
                if (cnt >= k) { ok = 1; break; }
            }
        }
        if (ok) lo = mid;
        else hi = mid - 1;
    }
    return lo;
}
