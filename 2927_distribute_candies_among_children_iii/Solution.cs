// LeetCode 2927 - Distribute Candies Among Children III
// https://leetcode.com/problems/distribute-candies-among-children-iii/

public class Solution {
    public long DistributeCandies(int n, int limit) {
        long Comb(long x) {
            if (x < 2) return 0;
            return x * (x - 1) / 2;
        }
        long ans = Comb((long)n + 2);
        ans -= 3 * Comb((long)(n - limit) + 1);
        ans += 3 * Comb((long)(n - 2 * (limit + 1)) + 2);
        ans -= Comb((long)(n - 3 * (limit + 1)) + 2);
        if (ans < 0) ans = 0;
        return ans;
    }
}
