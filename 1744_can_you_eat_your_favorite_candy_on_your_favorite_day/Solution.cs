// LeetCode 1744 - Can You Eat Your Favorite Candy on Your Favorite Day?
// https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/

public class Solution {
    public bool[] CanEat(int[] candiesCount, int[][] queries) {
        var prefix = new long[candiesCount.Length + 1];
        for (int i = 0; i < candiesCount.Length; i++) {
            prefix[i + 1] = prefix[i] + candiesCount[i];
        }
        var ans = new bool[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            int candyType = queries[i][0];
            long day = queries[i][1];
            long cap = queries[i][2];
            long minEaten = day + 1;
            long maxEaten = (day + 1) * cap;
            ans[i] = maxEaten > prefix[candyType] && minEaten <= prefix[candyType + 1];
        }
        return ans;
    }
}
