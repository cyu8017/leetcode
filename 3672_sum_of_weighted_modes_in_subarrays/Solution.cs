// LeetCode 3672 - Sum of Weighted Modes in Subarrays
// https://leetcode.com/problems/sum-of-weighted-modes-in-subarrays/

using System.Collections.Generic;

public class Solution {
    public long ModeWeight(int[] nums, int k) {
        var cnt = new Dictionary<int, int>();
        var pq = new PriorityQueue<int, (int, int)>();
        for (int i = 0; i < k; i++) {
            int x = nums[i];
            if (!cnt.ContainsKey(x)) cnt[x] = 0;
            cnt[x]++;
            pq.Enqueue(x, (-cnt[x], x));
        }
        long GetMode() {
            while (true) {
                pq.TryPeek(out int val, out var pri);
                int freq = -pri.Item1;
                if (cnt.GetValueOrDefault(val) == freq) return 1L * freq * val;
                pq.Dequeue();
            }
        }
        long ans = GetMode();
        for (int i = k; i < nums.Length; i++) {
            int x = nums[i], y = nums[i - k];
            if (!cnt.ContainsKey(x)) cnt[x] = 0;
            cnt[x]++;
            cnt[y]--;
            pq.Enqueue(x, (-cnt[x], x));
            pq.Enqueue(y, (-cnt[y], y));
            ans += GetMode();
        }
        return ans;
    }
}
