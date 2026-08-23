// LeetCode 0747 - Largest Number At Least Twice of Others
// https://leetcode.com/problems/largest-number-at-least-twice-of-others/

public class Solution {
    public int DominantIndex(int[] nums) {
        int first = -1, second = -1, index = -1;
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] > first) { second = first; first = nums[i]; index = i; }
            else if (nums[i] > second) second = nums[i];
        }
        return first >= 2 * second ? index : -1;
    }
}
