// LeetCode 3318 - Find X-Sum of All K-Long Subarrays I
// https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Solution {
    public int[] findXSum(int[] nums, int k, int x) {
        int n = nums.length;
        int[] ans = new int[n - k + 1];
        for (int i = 0; i <= n - k; i++) {
            Map<Integer, Integer> freq = new HashMap<>();
            for (int j = i; j < i + k; j++) freq.merge(nums[j], 1, Integer::sum);
            List<int[]> arr = new ArrayList<>();
            for (Map.Entry<Integer, Integer> p : freq.entrySet()) arr.add(new int[] {p.getKey(), p.getValue()});
            for (int a = 0; a < arr.size(); a++) {
                for (int b = a + 1; b < arr.size(); b++) {
                    int[] A = arr.get(a), B = arr.get(b);
                    if (B[1] > A[1] || (B[1] == A[1] && B[0] > A[0])) {
                        arr.set(a, B);
                        arr.set(b, A);
                    }
                }
            }
            int lim = Math.min(x, arr.size());
            Set<Integer> keep = new HashSet<>();
            for (int t = 0; t < lim; t++) keep.add(arr.get(t)[0]);
            int sum = 0;
            for (int j = i; j < i + k; j++) if (keep.contains(nums[j])) sum += nums[j];
            ans[i] = sum;
        }
        return ans;
    }
}
