// LeetCode 1744 - Can You Eat Your Favorite Candy on Your Favorite Day?
// https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/

class Solution {
    public boolean[] canEat(int[] candiesCount, int[][] queries) {
        long[] prefix = new long[candiesCount.length + 1];
        for (int i = 0; i < candiesCount.length; i++) {
            prefix[i + 1] = prefix[i] + candiesCount[i];
        }
        boolean[] ans = new boolean[queries.length];
        for (int i = 0; i < queries.length; i++) {
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
