// LeetCode 1893 - Check if All the Integers in a Range Are Covered
// https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

class Solution {
    public boolean isCovered(int[][] ranges, int left, int right) {
        boolean[] covered = new boolean[51];
        for (int[] range : ranges) {
            for (int value = range[0]; value <= range[1]; value++) {
                covered[value] = true;
            }
        }
        for (int value = left; value <= right; value++) {
            if (!covered[value]) {
                return false;
            }
        }
        return true;
    }
}
