// LeetCode 1460 - Make Two Arrays Equal By Reversing Subarrays
// https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/

using System.Linq;
public class Solution {
    public bool CanBeEqual(int[] target, int[] arr) {
        return target.OrderBy(x => x).SequenceEqual(arr.OrderBy(x => x));
    }
}
