// LeetCode 1385 - Find The Distance Value Between Two Arrays
// https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

using System;
public class Solution {
    public int FindTheDistanceValue(int[] arr1, int[] arr2, int d) {
        Array.Sort(arr2); int ans = 0;
        foreach (int x in arr1) {
            int i = Array.BinarySearch(arr2, x);
            if (i < 0) i = ~i;
            bool close = (i < arr2.Length && Math.Abs(arr2[i] - x) <= d) || (i > 0 && Math.Abs(arr2[i - 1] - x) <= d);
            if (!close) ans++;
        }
        return ans;
    }
}
