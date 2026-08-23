// LeetCode 3092 - Most Frequent IDs
// https://leetcode.com/problems/most-frequent-ids/

using System.Collections.Generic;

public class Solution {
    public long[] MostFrequentIDs(int[] nums, int[] freq) {
        int n = nums.Length;
        var cnt = new Dictionary<int, int>();
        var lazy = new Dictionary<int, int>();
        long[] ans = new long[n];
        var pq = new PriorityQueue<int, int>(Comparer<int>.Create((a, b) => b.CompareTo(a)));
        for (int i = 0; i < n; i++) {
            int x = nums[i], f = freq[i];
            if (!cnt.ContainsKey(x)) cnt[x] = 0;
            int old = cnt[x];
            if (!lazy.ContainsKey(old)) lazy[old] = 0;
            lazy[old]++;
            cnt[x] += f;
            pq.Enqueue(cnt[x], cnt[x]);
            while (pq.Count > 0) {
                int top = pq.Peek();
                if (lazy.TryGetValue(top, out int lz) && lz > 0) {
                    lazy[top]--;
                    pq.Dequeue();
                } else break;
            }
            if (pq.Count > 0) ans[i] = pq.Peek();
        }
        return ans;
    }
}
