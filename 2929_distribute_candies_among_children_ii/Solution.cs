// LeetCode 2929 - Distribute Candies Among Children II
// https://leetcode.com/problems/distribute-candies-among-children-ii/

public class Solution {
    public long DistributeCandies(int n, int limit) {
        long Comb2(long x) {
            if (x < 0) return 0;
            return (x + 1) * (x + 2) / 2;
        }
        long ans = Comb2(n);
        ans -= 3 * Comb2(n - (limit + 1));
        ans += 3 * Comb2(n - 2 * (limit + 1));
        ans -= Comb2(n - 3 * (limit + 1));
        return ans;
    }
}
