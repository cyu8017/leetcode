// LeetCode 2154 - Keep Multiplying Found Values by Two
// https://leetcode.com/problems/keep-multiplying-found-values-by-two/

public class Solution {
    public int FindFinalValue(int[] nums, int original) {
        var have = new HashSet<int>(nums);
        while (have.Contains(original)) original *= 2;
        return original;
    }
}
