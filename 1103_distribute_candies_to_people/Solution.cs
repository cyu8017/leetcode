// LeetCode 1103 - Distribute Candies to People
// https://leetcode.com/problems/distribute-candies-to-people/

using System;

public class Solution {
    public int[] DistributeCandies(int candies, int num_people) {
        int[] ans = new int[num_people];
        int give = 1;
        int i = 0;
        while (candies > 0) {
            int take = Math.Min(give, candies);
            ans[i] += take;
            candies -= take;
            give++;
            i = (i + 1) % num_people;
        }
        return ans;
    }
}
