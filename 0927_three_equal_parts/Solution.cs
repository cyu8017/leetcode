// LeetCode 0927 - Three Equal Parts
// https://leetcode.com/problems/three-equal-parts/

using System.Collections.Generic;

public class Solution {
    public int[] ThreeEqualParts(int[] arr) {
        var ones = new List<int>();
        for (int i = 0; i < arr.Length; i++) if (arr[i] != 0) ones.Add(i);
        int n = ones.Count;
        if (n % 3 != 0) return new[] { -1, -1 };
        if (n == 0) return new[] { 0, arr.Length - 1 };
        int third = n / 3;
        int length = ones[ones.Count - 1] - ones[2 * third] + 1;
        int a = ones[0], b = ones[third], c = ones[2 * third];
        if (a + length > arr.Length || b + length > arr.Length || c + length > arr.Length)
            return new[] { -1, -1 };
        for (int i = 0; i < length; i++) {
            if (arr[a + i] != arr[b + i] || arr[a + i] != arr[c + i]) return new[] { -1, -1 };
        }
        return new[] { a + length - 1, b + length };
    }
}
