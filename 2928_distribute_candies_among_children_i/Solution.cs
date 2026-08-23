// LeetCode 2928 - Distribute Candies Among Children I
// https://leetcode.com/problems/distribute-candies-among-children-i/

public class Solution {
    public int DistributeCandies(int n, int limit) {
        int ans = 0;
        for (int i = 0; i <= limit; i++)
            for (int j = 0; j <= limit; j++) {
                int k = n - i - j;
                if (k >= 0 && k <= limit) ans++;
            }
        return ans;
    }
}
