// LeetCode 1649 - Create Sorted Array through Instructions
// https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution {
    private static final int MOD = 1_000_000_007;

    public int createSortedArray(int[] instructions) {
        int size = 0;
        for (int x : instructions) size = Math.max(size, x);
        size += 2;
        int[] bit = new int[size + 1];
        long ans = 0;
        for (int i = 0; i < instructions.length; i++) {
            int x = instructions[i];
            ans = (ans + Math.min(query(bit, x - 1), i - query(bit, x))) % MOD;
            for (int j = x; j <= size; j += j & -j) bit[j]++;
        }
        return (int) ans;
    }

    private int query(int[] bit, int i) {
        int s = 0;
        while (i > 0) {
            s += bit[i];
            i -= i & -i;
        }
        return s;
    }
}
