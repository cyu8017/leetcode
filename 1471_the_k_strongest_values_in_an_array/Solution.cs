// LeetCode 1471 - The K Strongest Values In An Array
// https://leetcode.com/problems/the-k-strongest-values-in-an-array/

using System;
using System.Linq;
public class Solution {
    public int[] GetStrongest(int[] arr, int k) {
        Array.Sort(arr);
        int median = arr[(arr.Length - 1) / 2];
        return arr.OrderByDescending(x => Math.Abs(x - median)).ThenByDescending(x => x).Take(k).ToArray();
    }
}
