// LeetCode 3935 - Power Update After K Th Largest Insertion I
// https://leetcode.com/problems/power-update-after-k-th-largest-insertion-i/

import java.util.TreeMap;

class Solution {
    private static void merge(TreeMap<Integer, Integer> st, int x, int v) {
        int c = st.getOrDefault(x, 0);
        if (c + v == 0) st.remove(x);
        else st.put(x, c + v);
    }

    public int[] powerUpdate(int[] nums, int p, int[][] queries) {
        TreeMap<Integer, Integer> L = new TreeMap<>();
        TreeMap<Integer, Integer> R = new TreeMap<>();
        int sz1 = 0, sz2 = nums.length;
        for (int x : nums) merge(R, x, 1);
        final int mod = 1000000007;
        int[] ans = new int[queries.length];
        for (int qi = 0; qi < queries.length; qi++) {
            int val = queries[qi][0], k = queries[qi][1];
            merge(R, val, 1);
            sz2++;
            int node = R.firstKey();
            merge(R, node, -1);
            sz2--;
            merge(L, node, 1);
            sz1++;
            while (sz2 < k) {
                node = L.lastKey();
                merge(L, node, -1);
                sz1--;
                merge(R, node, 1);
                sz2++;
            }
            while (sz2 > k) {
                node = R.firstKey();
                merge(R, node, -1);
                sz2--;
                merge(L, node, 1);
                sz1++;
            }
            int x = R.firstKey();
            p = qpow(p, x, mod);
            ans[qi] = p;
        }
        return ans;
    }

    private static int qpow(long a, int b, int mod) {
        long ans = 1;
        while (b > 0) {
            if ((b & 1) != 0) ans = ans * a % mod;
            a = a * a % mod;
            b >>= 1;
        }
        return (int) ans;
    }
}
