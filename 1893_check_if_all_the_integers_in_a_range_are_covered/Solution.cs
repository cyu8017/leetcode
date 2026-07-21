// LeetCode 1893 - Check if All the Integers in a Range Are Covered
// https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

public class Solution {
    public bool IsCovered(int[][] ranges, int left, int right) {
        var covered = new bool[51];
        foreach (var r in ranges) {
            for (int value = r[0]; value <= r[1]; value++) {
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
