// LeetCode 1351 - Count Negative Numbers In A Sorted Matrix
// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

public class Solution {
    public int CountNegatives(int[][] grid) {
        int answer = 0;
        foreach (var row in grid) {
            int lo = 0, hi = row.Length;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (row[mid] < 0) hi = mid; else lo = mid + 1;
            }
            answer += row.Length - lo;
        }
        return answer;
    }
}
