// LeetCode 1276 - Number of Burgers with No Waste of Ingredients
// https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

public class Solution {
    public int[] NumOfBurgers(int tomatoSlices, int cheeseSlices) {
        if (tomatoSlices % 2 != 0) return new int[0];
        int jumbo = tomatoSlices / 2 - cheeseSlices;
        int small = cheeseSlices - jumbo;
        return jumbo >= 0 && small >= 0 ? new[] { jumbo, small } : new int[0];
    }
}
