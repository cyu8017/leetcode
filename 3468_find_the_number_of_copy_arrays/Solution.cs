// LeetCode 3468 - Find the Number of Copy Arrays
// https://leetcode.com/problems/find-the-number-of-copy-arrays/

public class Solution {
    public int CountArrays(int[] original, int[][] bounds) {
        int n = original.Length;
        int lo = bounds[0][0], hi = bounds[0][1];
        for (int i = 1; i < n; i++) {
            int diff = original[i] - original[i - 1];
            int lo2 = bounds[i][0], hi2 = bounds[i][1];
            int nlo = lo + diff, nhi = hi + diff;
            if (nlo < lo2) nlo = lo2;
            if (nhi > hi2) nhi = hi2;
            if (nlo > nhi) return 0;
            lo = nlo;
            hi = nhi;
        }
        return hi - lo + 1;
    }
}
