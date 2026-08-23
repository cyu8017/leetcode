// LeetCode 3048 - Earliest Second to Mark Indices I
// https://leetcode.com/problems/earliest-second-to-mark-indices-i/

public class Solution {
    public int EarliestSecondToMarkIndices(int[] nums, int[] changeIndices) {
        int n = nums.Length, m = changeIndices.Length;
        bool Ok(int t) {
            int[] last = new int[n + 1];
            for (int s = 0; s < t; s++) last[changeIndices[s]] = s;
            int decrement = 0, marked = 0;
            for (int s = 0; s < t; s++) {
                int i = changeIndices[s];
                if (last[i] == s) {
                    if (decrement < nums[i - 1]) return false;
                    decrement -= nums[i - 1];
                    marked++;
                } else {
                    decrement++;
                }
            }
            return marked == n;
        }
        int l = 0, r = m + 1;
        while (l < r) {
            int mid = (l + r) / 2;
            if (Ok(mid)) r = mid;
            else l = mid + 1;
        }
        return l > m ? -1 : l;
    }
}
