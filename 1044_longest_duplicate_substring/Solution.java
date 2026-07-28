// LeetCode 1044 - Longest Duplicate Substring
// https://leetcode.com/problems/longest-duplicate-substring/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE = 911382323L;

    public String longestDupSubstring(String s) {
        int n = s.length();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = s.charAt(i);
        int lo = 0, hi = n - 1, start = -1, bestLen = 0;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            int pos = search(s, nums, mid);
            if (pos >= 0) {
                start = pos;
                bestLen = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return start < 0 ? "" : s.substring(start, start + bestLen);
    }

    private int search(String s, int[] nums, int length) {
        if (length == 0) return 0;
        int n = nums.length;
        long h = 0, power = 1;
        for (int i = 0; i < length; i++) {
            h = (h * BASE + nums[i]) % MOD;
            power = power * BASE % MOD;
        }
        Map<Long, List<Integer>> seen = new HashMap<>();
        seen.computeIfAbsent(h, k -> new ArrayList<>()).add(0);
        for (int i = 1; i + length - 1 < n; i++) {
            h = (h * BASE - nums[i - 1] * power % MOD + MOD) % MOD;
            h = (h + nums[i + length - 1]) % MOD;
            List<Integer> idxs = seen.get(h);
            if (idxs != null) {
                String cur = s.substring(i, i + length);
                for (int j : idxs) {
                    if (s.substring(j, j + length).equals(cur)) return i;
                }
                idxs.add(i);
            } else {
                List<Integer> list = new ArrayList<>();
                list.add(i);
                seen.put(h, list);
            }
        }
        return -1;
    }
}
