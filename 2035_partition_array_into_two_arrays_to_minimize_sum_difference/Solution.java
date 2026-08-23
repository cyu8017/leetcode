// LeetCode 2035 - Partition Array Into Two Arrays to Minimize Sum Difference
// https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/

import java.util.*;

class Solution {
    public int minimumDifference(int[] nums) {
        int n = nums.length / 2;
        int total = 0;
        for (int v : nums) total += v;
        int[] left = Arrays.copyOfRange(nums, 0, n);
        int[] right = Arrays.copyOfRange(nums, n, nums.length);
        List<Integer>[] L = sumsByCount(left);
        List<Integer>[] R = sumsByCount(right);
        int ans = Integer.MAX_VALUE;
        for (int k = 0; k <= n; k++) {
            for (int s1 : L[k]) {
                int need = total / 2 - s1;
                List<Integer> arr = R[n - k];
                int idx = Collections.binarySearch(arr, need);
                if (idx < 0) idx = -idx - 1;
                for (int j : new int[] { idx - 1, idx }) {
                    if (j >= 0 && j < arr.size()) {
                        int s2 = arr.get(j);
                        ans = Math.min(ans, Math.abs(total - 2 * (s1 + s2)));
                    }
                }
            }
        }
        return ans;
    }

    private List<Integer>[] sumsByCount(int[] arr) {
        int m = arr.length;
        @SuppressWarnings("unchecked")
        List<Integer>[] res = new ArrayList[m + 1];
        for (int i = 0; i <= m; i++) res[i] = new ArrayList<>();
        for (int mask = 0; mask < (1 << m); mask++) {
            int sum = 0, c = 0;
            for (int i = 0; i < m; i++) if ((mask & (1 << i)) != 0) { sum += arr[i]; c++; }
            res[c].add(sum);
        }
        for (List<Integer> v : res) Collections.sort(v);
        return res;
    }
}
