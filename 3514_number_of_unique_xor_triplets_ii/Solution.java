// LeetCode 3514 - Number of Unique XOR Triplets II
// https://leetcode.com/problems/number-of-unique-xor-triplets-ii/

class Solution {
    public int uniqueXorTriplets(int[] nums) {
        int mx = 0;
        for (int v : nums) mx = Math.max(mx, v);
        mx <<= 1;
        boolean[] st = new boolean[mx];
        for (int a : nums) for (int b : nums) st[a ^ b] = true;
        int[] s = new int[mx];
        for (int ab = 0; ab < mx; ab++) {
            if (st[ab]) for (int c : nums) s[ab ^ c] = 1;
        }
        int ans = 0;
        for (int v : s) ans += v;
        return ans;
    }
}
