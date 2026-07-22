// LeetCode 1649 - Create Sorted Array through Instructions
// https://leetcode.com/problems/create-sorted-array-through-instructions/

using System;
using System.Linq;

public class Solution {
    public int CreateSortedArray(int[] instructions) {
        const int MOD = 1000000007;
        int size = instructions.Max() + 2;
        var bit = new int[size + 1];
        int Query(int i) {
            int s = 0;
            while (i > 0) { s += bit[i]; i -= i & -i; }
            return s;
        }
        void Update(int i) {
            while (i <= size) { bit[i]++; i += i & -i; }
        }
        int ans = 0;
        for (int i = 0; i < instructions.Length; i++) {
            int x = instructions[i];
            ans = (ans + Math.Min(Query(x - 1), i - Query(x))) % MOD;
            Update(x);
        }
        return ans;
    }
}
