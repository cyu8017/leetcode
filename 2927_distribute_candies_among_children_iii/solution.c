// LeetCode 2927 - Distribute Candies Among Children III
// https://leetcode.com/problems/distribute-candies-among-children-iii/

static long long comb(long long x) {
    if (x < 2) return 0;
    return x * (x - 1) / 2;
}

long long distributeCandies(int n, int limit) {
    long long ans = comb((long long)n + 2);
    ans -= 3 * comb((long long)(n - limit) + 1);
    ans += 3 * comb((long long)(n - 2 * (limit + 1)) + 2);
    ans -= comb((long long)(n - 3 * (limit + 1)) + 2);
    if (ans < 0) ans = 0;
    return ans;
}
