// LeetCode 1608 - Special Array With X Elements Greater Than or Equal X
// https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

using System.Linq;

public class Solution {
    public int SpecialArray(int[] nums) {
        for (int x = 0; x <= nums.Length; x++) {
            if (nums.Count(v => v >= x) == x) return x;
        }
        return -1;
    }
}
