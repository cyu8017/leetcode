// LeetCode 2709 - Greatest Common Divisor Traversal
// https://leetcode.com/problems/greatest-common-divisor-traversal/

using System;

public class Solution {
    public bool CanTraverseAllPairs(int[] nums) {
        int n = nums.Length;
        if (n == 1) return true;
        int mx = nums[0];
        foreach (int x in nums) if (x > mx) mx = x;
        int[] parent = new int[mx + 1];
        for (int i = 0; i <= mx; i++) parent[i] = i;
        int Find(int x) {
            if (parent[x] != x) parent[x] = Find(parent[x]);
            return parent[x];
        }
        void Unite(int a, int b) {
            int ra = Find(a), rb = Find(b);
            if (ra != rb) parent[ra] = rb;
        }
        bool[] has = new bool[mx + 1];
        foreach (int x in nums) {
            if (x == 1) return false;
            has[x] = true;
        }
        int[] sieve = new int[mx + 1];
        for (int i = 2; i <= mx; i++) {
            if (sieve[i] == 0) {
                for (int j = i; j <= mx; j += i) {
                    if (sieve[j] == 0) sieve[j] = i;
                    if (has[j]) Unite(i, j);
                }
            }
        }
        int root = Find(nums[0]);
        foreach (int x in nums) if (Find(x) != root) return false;
        return true;
    }
}
