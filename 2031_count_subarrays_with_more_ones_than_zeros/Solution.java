// LeetCode 2031 - Count Subarrays With More Ones Than Zeros
// https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/

class Solution {
    private static class Fenwick {
        private final int[] bit;
        Fenwick(int n) { bit = new int[n + 2]; }
        void add(int i, int v) { for (; i < bit.length; i += i & -i) bit[i] += v; }
        int sum(int i) { int s = 0; for (; i > 0; i -= i & -i) s += bit[i]; return s; }
    }

    public int subarraysWithMoreZerosThanOnes(int[] nums) {
        final int MOD = 1_000_000_007;
        int n = nums.length, offset = n + 1;
        Fenwick fw = new Fenwick(2 * n + 5);
        int pref = 0, ans = 0;
        fw.add(offset, 1);
        for (int x : nums) {
            pref += (x == 1) ? 1 : -1;
            int idx = pref + offset;
            ans = (ans + fw.sum(idx - 1)) % MOD;
            fw.add(idx, 1);
        }
        return ans;
    }
}
