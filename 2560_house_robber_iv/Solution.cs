// LeetCode 2560 - House Robber IV
// https://leetcode.com/problems/house-robber-iv/

using System.Linq;

public class Solution {
    public int MinCapability(int[] nums, int k) {
        int lo = nums.Min();
        int hi = nums.Max();
        bool Ok(int cap) {
            int cnt = 0;
            for (int i = 0; i < nums.Length;) {
                if (nums[i] <= cap) {
                    cnt++;
                    i += 2;
                } else {
                    i++;
                }
            }
            return cnt >= k;
        }
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (Ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
