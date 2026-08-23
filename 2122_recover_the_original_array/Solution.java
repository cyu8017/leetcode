// LeetCode 2122 - Recover the Original Array
// https://leetcode.com/problems/recover-the-original-array/

import java.util.*;

class Solution {
    public int[] recoverArray(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        for (int i = 1; i < n; i++) {
            int diff = nums[i] - nums[0];
            if (diff == 0 || diff % 2 != 0) continue;
            int k = diff / 2;
            boolean[] used = new boolean[n];
            used[0] = used[i] = true;
            List<Integer> ans = new ArrayList<>();
            ans.add((nums[0] + nums[i]) / 2);
            int l = 0, r = i;
            boolean ok = true;
            while (ans.size() < n / 2) {
                while (l < n && used[l]) l++;
                if (l == n) { ok = false; break; }
                int need = nums[l] + 2 * k;
                while (r < n && (used[r] || nums[r] < need)) r++;
                if (r == n || nums[r] != need) { ok = false; break; }
                used[l] = used[r] = true;
                ans.add(nums[l] + k);
            }
            if (ok) {
                int[] res = new int[ans.size()];
                for (int t = 0; t < ans.size(); t++) res[t] = ans.get(t);
                return res;
            }
        }
        return new int[0];
    }
}
