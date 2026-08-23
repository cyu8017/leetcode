// LeetCode 2111 - Minimum Operations to Make the Array K-Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/

import java.util.*;

class Solution {
    public int kIncreasing(int[] arr, int k) {
        int ans = 0, n = arr.length;
        for (int start = 0; start < k; start++) {
            List<Integer> seq = new ArrayList<>();
            for (int i = start; i < n; i += k) seq.add(arr[i]);
            List<Integer> tails = new ArrayList<>();
            for (int x : seq) {
                int lo = 0, hi = tails.size();
                while (lo < hi) {
                    int mid = (lo + hi) / 2;
                    if (tails.get(mid) <= x) lo = mid + 1;
                    else hi = mid;
                }
                if (lo == tails.size()) tails.add(x);
                else tails.set(lo, x);
            }
            ans += seq.size() - tails.size();
        }
        return ans;
    }
}
