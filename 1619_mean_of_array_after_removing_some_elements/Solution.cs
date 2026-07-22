// LeetCode 1619 - Mean of Array After Removing Some Elements
// https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

using System;
using System.Linq;

public class Solution {
    public double TrimMean(int[] arr) {
        Array.Sort(arr);
        int k = arr.Length / 20;
        return arr.Skip(k).Take(arr.Length - 2 * k).Average();
    }
}
