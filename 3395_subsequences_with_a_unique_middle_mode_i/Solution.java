// LeetCode 3395 - Subsequences with a Unique Middle Mode I
// https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private boolean uniqueMode(int[] a) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int x : a) freq.merge(x, 1, Integer::sum);
        int best = 0, cnt = 0;
        for (int f : freq.values()) {
            if (f > best) { best = f; cnt = 1; }
            else if (f == best) cnt++;
        }
        return cnt == 1;
    }

    public int subsequencesWithMiddleMode(int[] nums) {
        final int mod = 1_000_000_007;
        int n = nums.length;
        int ans = 0;
        for (int mid = 2; mid < n - 2; mid++) {
            for (int a = 0; a < mid; a++) {
                for (int b = a + 1; b < mid; b++) {
                    for (int c = mid + 1; c < n; c++) {
                        for (int d = c + 1; d < n; d++) {
                            int[] seq = {nums[a], nums[b], nums[mid], nums[c], nums[d]};
                            if (uniqueMode(seq)) ans++;
                        }
                    }
                }
            }
        }
        return ans % mod;
    }
}
