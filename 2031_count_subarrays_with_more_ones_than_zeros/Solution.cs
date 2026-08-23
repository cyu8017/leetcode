// LeetCode 2031 - Count Subarrays With More Ones Than Zeros
// https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/

public class Solution {
    private class Fenwick {
        private readonly int[] bit;
        public Fenwick(int n) { bit = new int[n + 2]; }
        public void Add(int i, int v) { for (; i < bit.Length; i += i & -i) bit[i] += v; }
        public int Sum(int i) { int s = 0; for (; i > 0; i -= i & -i) s += bit[i]; return s; }
    }

    public int SubarraysWithMoreZerosThanOnes(int[] nums) {
        const int MOD = 1000000007;
        int n = nums.Length, offset = n + 1;
        var fw = new Fenwick(2 * n + 5);
        int pref = 0, ans = 0;
        fw.Add(offset, 1);
        foreach (int x in nums) {
            pref += (x == 1) ? 1 : -1;
            int idx = pref + offset;
            ans = (ans + fw.Sum(idx - 1)) % MOD;
            fw.Add(idx, 1);
        }
        return ans;
    }
}
