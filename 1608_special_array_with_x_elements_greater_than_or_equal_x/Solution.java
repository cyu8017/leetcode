// LeetCode 1608 - Special Array With X Elements Greater Than or Equal X
// https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

class Solution {
    public int specialArray(int[] nums) {
        for (int x = 0; x <= nums.length; x++) {
            int count = 0;
            for (int v : nums) if (v >= x) count++;
            if (count == x) return x;
        }
        return -1;
    }
}
