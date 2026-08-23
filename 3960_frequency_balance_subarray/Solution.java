// LeetCode 3960 - Frequency Balance Subarray
// https://leetcode.com/problems/frequency-balance-subarray/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int getLength(int[] nums) {
        int n = nums.length;
        int ans = 1;
        for (int l = 0; l < n; l++) {
            Map<Integer, Integer> cnt = new HashMap<>();
            Map<Integer, Integer> freq = new HashMap<>();
            for (int r = l; r < n; r++) {
                int x = nums[r];
                int c = cnt.getOrDefault(x, 0);
                if (freq.getOrDefault(c, 0) > 0) {
                    int fc = freq.get(c) - 1;
                    if (fc == 0) freq.remove(c);
                    else freq.put(c, fc);
                }
                cnt.put(x, c + 1);
                freq.put(cnt.get(x), freq.getOrDefault(cnt.get(x), 0) + 1);
                int cx = cnt.get(x);
                if (cnt.size() == 1 || (freq.size() == 2 && (freq.getOrDefault(cx * 2, 0) > 0 || (cx % 2 == 0 && freq.getOrDefault(cx / 2, 0) > 0)))) {
                    ans = Math.max(ans, r - l + 1);
                }
            }
        }
        return ans;
    }
}
