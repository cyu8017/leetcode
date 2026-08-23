// LeetCode 2545 - Sort the Students by Their Kth Score
// https://leetcode.com/problems/sort-the-students-by-their-kth-score/

using System;

public class Solution {
    public int[][] SortTheStudents(int[][] score, int k) {
        Array.Sort(score, (a, b) => b[k].CompareTo(a[k]));
        return score;
    }
}
