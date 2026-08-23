// LeetCode 3930 - Power Update After K-th Largest Insertion II
// https://leetcode.com/problems/power-update-after-k-th-largest-insertion-ii/

using System.Collections.Generic;

public class Solution {
    public int[] PowerUpdate(int[] nums, int p, int[][] queries) {
        const long mod = 1000000007;
        var vals = new List<int>(nums);
        foreach (var q in queries) vals.Add(q[0]);
        vals.Sort();
        int w = 0;
        for (int i = 0; i < vals.Count; i++) {
            if (i == 0 || vals[i] != vals[i - 1]) vals[w++] = vals[i];
        }
        vals.RemoveRange(w, vals.Count - w);
        int[] bit = new int[vals.Count + 1];
        void Add(int i) {
            for (; i < bit.Length; i += i & -i) bit[i]++;
        }
        int Kth(int rank) {
            int idx = 0;
            int step = 1;
            while ((step << 1) < bit.Length) step <<= 1;
            for (; step > 0; step >>= 1) {
                int next = idx + step;
                if (next < bit.Length && bit[next] < rank) {
                    idx = next;
                    rank -= bit[next];
                }
            }
            return vals[idx];
        }
        int LowerBound(int x) {
            int lo = 0, hi = vals.Count;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (vals[mid] < x) lo = mid + 1;
                else hi = mid;
            }
            return lo;
        }
        foreach (int x in nums) Add(LowerBound(x) + 1);
        long Powm(long a, long e) {
            long res = 1;
            while (e > 0) {
                if ((e & 1) != 0) res = res * a % mod;
                a = a * a % mod;
                e >>= 1;
            }
            return res;
        }
        int[] ans = new int[queries.Length];
        int size = nums.Length;
        long cur = p;
        for (int i = 0; i < queries.Length; i++) {
            Add(LowerBound(queries[i][0]) + 1);
            size++;
            int x = Kth(size - queries[i][1] + 1);
            cur = Powm(cur, x);
            ans[i] = (int)cur;
        }
        return ans;
    }
}
