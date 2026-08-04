// LeetCode 1351 - Count Negative Numbers In A Sorted Matrix
// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution {
    public int countNegatives(int[][] grid) {
        int answer = 0;
        for (var row : grid) {
            int lo = 0, hi = row.length;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (row[mid] < 0) hi = mid; else lo = mid + 1;
            }
            answer += row.length - lo;
        }
        return answer;
    }
}
