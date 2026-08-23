// LeetCode 3533 - Concatenated Divisibility
// https://leetcode.com/problems/concatenated-divisibility/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    int n, k;
    int[] nums, pows;
    Map<Long, Boolean> memo;

    public int[] concatenatedDivisibility(int[] nums, int k) {
        Arrays.sort(nums);
        this.nums = nums;
        this.k = k;
        n = nums.length;
        pows = new int[n];
        for (int i = 0; i < n; i++) {
            int p = 1, num = nums[i];
            if (num == 0) p = 10 % k;
            else {
                for (int x = num; x > 0; x /= 10) p = p * 10 % k;
            }
            pows[i] = p;
        }
        memo = new HashMap<>();
        if (!dp(0, 0)) return new int[0];
        List<Integer> res = reconstruct(0, 0);
        return res.stream().mapToInt(Integer::intValue).toArray();
    }

    boolean dp(int mask, int mod) {
        if (mask == (1 << n) - 1) return mod == 0;
        long key = ((long) mask << 32) | mod;
        if (memo.containsKey(key)) return memo.get(key);
        for (int i = 0; i < n; i++) {
            if (((mask >> i) & 1) == 0) {
                int nm = (mod * pows[i] + nums[i]) % k;
                if (dp(mask | (1 << i), nm)) {
                    memo.put(key, true);
                    return true;
                }
            }
        }
        memo.put(key, false);
        return false;
    }

    List<Integer> reconstruct(int mask, int mod) {
        for (int i = 0; i < n; i++) {
            if (((mask >> i) & 1) == 0) {
                int nm = (mod * pows[i] + nums[i]) % k;
                if (dp(mask | (1 << i), nm)) {
                    List<Integer> rest = reconstruct(mask | (1 << i), nm);
                    rest.add(0, nums[i]);
                    return rest;
                }
            }
        }
        return new ArrayList<>();
    }
}
