// LeetCode 3935 - Power Update After K Th Largest Insertion I
// https://leetcode.com/problems/power-update-after-k-th-largest-insertion-i/

using System.Collections.Generic;

public class Solution {
    static void Merge(SortedDictionary<int, int> st, int x, int v) {
        int c = st.TryGetValue(x, out int cur) ? cur : 0;
        if (c + v == 0) st.Remove(x);
        else st[x] = c + v;
    }

    public int[] PowerUpdate(int[] nums, int p, int[][] queries) {
        var L = new SortedDictionary<int, int>();
        var R = new SortedDictionary<int, int>();
        int sz1 = 0, sz2 = nums.Length;
        foreach (int x in nums) Merge(R, x, 1);
        const int mod = 1000000007;
        int Qpow(long a, int b) {
            long ans = 1;
            while (b > 0) {
                if ((b & 1) != 0) ans = ans * a % mod;
                a = a * a % mod;
                b >>= 1;
            }
            return (int)ans;
        }
        var ans = new List<int>(queries.Length);
        foreach (var q in queries) {
            int val = q[0], k = q[1];
            Merge(R, val, 1);
            sz2++;
            int node = FirstKey(R);
            Merge(R, node, -1);
            sz2--;
            Merge(L, node, 1);
            sz1++;
            while (sz2 < k) {
                node = LastKey(L);
                Merge(L, node, -1);
                sz1--;
                Merge(R, node, 1);
                sz2++;
            }
            while (sz2 > k) {
                node = FirstKey(R);
                Merge(R, node, -1);
                sz2--;
                Merge(L, node, 1);
                sz1++;
            }
            int x = FirstKey(R);
            p = Qpow(p, x);
            ans.Add(p);
        }
        return ans.ToArray();
    }

    static int FirstKey(SortedDictionary<int, int> st) {
        foreach (var kv in st) return kv.Key;
        return 0;
    }

    static int LastKey(SortedDictionary<int, int> st) {
        int last = 0;
        foreach (var kv in st) last = kv.Key;
        return last;
    }
}
