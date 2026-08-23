// LeetCode 2607 - Make K-Subarray Sums Equal
// https://leetcode.com/problems/make-k-subarray-sums-equal/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public long makeSubKSumEqual(int[] arr, int k) {
        int n = arr.length;
        int g = gcd(n, k);
        long ans = 0;
        for (int r = 0; r < g; ++r) {
            List<Integer> group = new ArrayList<>();
            for (int i = r; i < n; i += g) group.add(arr[i]);
            Collections.sort(group);
            int med = group.get(group.size() / 2);
            for (int x : group) ans += Math.abs(x - med);
        }
        return ans;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
