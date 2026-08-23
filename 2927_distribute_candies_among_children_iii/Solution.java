// LeetCode 2927 - Distribute Candies Among Children III
// https://leetcode.com/problems/distribute-candies-among-children-iii/

class Solution {
    public long distributeCandies(int n, int limit) {
        long ans = comb(n + 2L);
        ans -= 3 * comb((long) (n - limit) + 1);
        ans += 3 * comb((long) (n - 2 * (limit + 1)) + 2);
        ans -= comb((long) (n - 3 * (limit + 1)) + 2);
        if (ans < 0) ans = 0;
        return ans;
    }

    private long comb(long x) {
        if (x < 2) return 0;
        return x * (x - 1) / 2;
    }
}
