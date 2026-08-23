// LeetCode 1103 - Distribute Candies to People
// https://leetcode.com/problems/distribute-candies-to-people/

class Solution {
    public int[] distributeCandies(int candies, int num_people) {
        int[] ans = new int[num_people];
        int give = 1, i = 0;
        while (candies > 0) {
            int take = Math.min(give, candies);
            ans[i] += take;
            candies -= take;
            give++;
            i = (i + 1) % num_people;
        }
        return ans;
    }
}
