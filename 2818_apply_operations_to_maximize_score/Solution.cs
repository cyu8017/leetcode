// LeetCode 2818 - Apply Operations to Maximize Score
// https://leetcode.com/problems/apply-operations-to-maximize-score/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaximumScore(IList<int> nums, int k) {
        const int MOD = 1000000007;
        int n = nums.Count;
        int maxV = 0;
        foreach (int v in nums) maxV = Math.Max(maxV, v);
        int[] spf = new int[maxV + 1];
        for (int i = 2; i <= maxV; i++) {
            if (spf[i] == 0) {
                for (int j = i; j <= maxV; j += i) if (spf[j] == 0) spf[j] = i;
            }
        }
        int PrimeScore(int x) {
            var seen = new HashSet<int>();
            while (x > 1) {
                int p = spf[x];
                seen.Add(p);
                while (x % p == 0) x /= p;
            }
            return seen.Count;
        }
        int[] score = new int[n];
        for (int i = 0; i < n; i++) score[i] = PrimeScore(nums[i]);
        int[] left = new int[n], right = new int[n];
        var st = new List<int>();
        for (int i = 0; i < n; i++) {
            while (st.Count > 0 && score[st[^1]] < score[i]) st.RemoveAt(st.Count - 1);
            left[i] = st.Count == 0 ? -1 : st[^1];
            st.Add(i);
        }
        st.Clear();
        for (int i = n - 1; i >= 0; i--) {
            while (st.Count > 0 && score[st[^1]] <= score[i]) st.RemoveAt(st.Count - 1);
            right[i] = st.Count == 0 ? n : st[^1];
            st.Add(i);
        }
        var arr = new (int v, long cnt)[n];
        for (int i = 0; i < n; i++)
            arr[i] = (nums[i], 1L * (i - left[i]) * (right[i] - i));
        Array.Sort(arr, (a, b) => b.v.CompareTo(a.v));
        long ModPow(long a, long b) {
            long res = 1;
            a %= MOD;
            while (b > 0) {
                if ((b & 1) != 0) res = res * a % MOD;
                a = a * a % MOD;
                b >>= 1;
            }
            return res;
        }
        long ans = 1;
        long remain = k;
        foreach (var (v, cnt) in arr) {
            if (remain <= 0) break;
            long use = Math.Min(cnt, remain);
            ans = ans * ModPow(v, use) % MOD;
            remain -= use;
        }
        return (int)ans;
    }
}
