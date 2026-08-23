// LeetCode 3835 - Count Subarrays With Cost Less Than Or Equal To K
// https://leetcode.com/problems/count-subarrays-with-cost-less-than-or-equal-to-k/

using System.Collections.Generic;

public class Solution {
    public long CountSubarrays(int[] nums, long k) {
        long ans = 0;
        var q1 = new LinkedList<int>();
        var q2 = new LinkedList<int>();
        int l = 0;
        for (int r = 0; r < nums.Length; r++) {
            int x = nums[r];
            while (q1.Count > 0 && nums[q1.Last.Value] <= x) q1.RemoveLast();
            while (q2.Count > 0 && nums[q2.Last.Value] >= x) q2.RemoveLast();
            q1.AddLast(r);
            q2.AddLast(r);
            while (l < r && (long)(nums[q1.First.Value] - nums[q2.First.Value]) * (r - l + 1) > k) {
                l++;
                if (q1.First.Value < l) q1.RemoveFirst();
                if (q2.First.Value < l) q2.RemoveFirst();
            }
            ans += r - l + 1;
        }
        return ans;
    }
}
