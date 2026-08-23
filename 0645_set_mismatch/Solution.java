// LeetCode 0645 - Set Mismatch
// https://leetcode.com/problems/set-mismatch/

class Solution {
    public int[] findErrorNums(int[] nums) {
        int n = nums.length;
        int[] seen = new int[n + 1];
        int duplicate = -1;
        int missing = -1;
        for (int value : nums) {
            ++seen[value];
        }
        for (int value = 1; value <= n; ++value) {
            if (seen[value] == 2) {
                duplicate = value;
            } else if (seen[value] == 0) {
                missing = value;
            }
        }
        return new int[] {duplicate, missing};
    }
}
