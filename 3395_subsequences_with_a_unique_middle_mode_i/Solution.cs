// LeetCode 3395 - Subsequences with a Unique Middle Mode I
// https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/

using System.Collections.Generic;

public class Solution {
    bool UniqueMode(int[] a) {
        var freq = new Dictionary<int, int>();
        foreach (int x in a) {
            freq.TryGetValue(x, out int f);
            freq[x] = f + 1;
        }
        int best = 0, cnt = 0;
        foreach (var kv in freq) {
            if (kv.Value > best) { best = kv.Value; cnt = 1; }
            else if (kv.Value == best) cnt++;
        }
        return cnt == 1;
    }

    public int SubsequencesWithMiddleMode(int[] nums) {
        const int mod = 1000000007;
        int n = nums.Length;
        int ans = 0;
        for (int mid = 2; mid < n - 2; mid++) {
            for (int a = 0; a < mid; a++) {
                for (int b = a + 1; b < mid; b++) {
                    for (int c = mid + 1; c < n; c++) {
                        for (int d = c + 1; d < n; d++) {
                            int[] seq = { nums[a], nums[b], nums[mid], nums[c], nums[d] };
                            if (UniqueMode(seq)) ans++;
                        }
                    }
                }
            }
        }
        return ans % mod;
    }
}
