// LeetCode 2818 - Apply Operations to Maximize Score
// https://leetcode.com/problems/apply-operations-to-maximize-score/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    private static final int MOD = 1_000_000_007;

    public int maximumScore(List<Integer> nums, int k) {
        int n = nums.size();
        int maxV = 0;
        for (int v : nums) maxV = Math.max(maxV, v);
        int[] spf = new int[maxV + 1];
        for (int i = 2; i <= maxV; i++) {
            if (spf[i] == 0) {
                for (int j = i; j <= maxV; j += i) if (spf[j] == 0) spf[j] = i;
            }
        }
        int[] score = new int[n];
        for (int i = 0; i < n; i++) score[i] = primeScore(nums.get(i), spf);
        int[] left = new int[n], right = new int[n];
        List<Integer> st = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            while (!st.isEmpty() && score[st.get(st.size() - 1)] < score[i]) st.remove(st.size() - 1);
            left[i] = st.isEmpty() ? -1 : st.get(st.size() - 1);
            st.add(i);
        }
        st.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!st.isEmpty() && score[st.get(st.size() - 1)] <= score[i]) st.remove(st.size() - 1);
            right[i] = st.isEmpty() ? n : st.get(st.size() - 1);
            st.add(i);
        }
        long[][] arr = new long[n][2];
        for (int i = 0; i < n; i++) {
            arr[i][0] = nums.get(i);
            arr[i][1] = 1L * (i - left[i]) * (right[i] - i);
        }
        Arrays.sort(arr, (a, b) -> Long.compare(b[0], a[0]));
        long ans = 1;
        long remain = k;
        for (long[] pair : arr) {
            if (remain <= 0) break;
            long use = Math.min(pair[1], remain);
            ans = ans * modPow(pair[0], use) % MOD;
            remain -= use;
        }
        return (int) ans;
    }

    private int primeScore(int x, int[] spf) {
        Set<Integer> seen = new HashSet<>();
        while (x > 1) {
            int p = spf[x];
            seen.add(p);
            while (x % p == 0) x /= p;
        }
        return seen.size();
    }

    private long modPow(long a, long b) {
        long res = 1;
        a %= MOD;
        while (b > 0) {
            if ((b & 1) != 0) res = res * a % MOD;
            a = a * a % MOD;
            b >>= 1;
        }
        return res;
    }
}
