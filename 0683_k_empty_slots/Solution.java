// LeetCode 0683 - K Empty Slots
// https://leetcode.com/problems/k-empty-slots/

class Solution {
    public int kEmptySlots(int[] bulbs, int k) {
        int n = bulbs.length;
        int[] days = new int[n];
        for (int day = 1; day <= n; day++) days[bulbs[day - 1] - 1] = day;
        int ans = Integer.MAX_VALUE;
        int i = 0;
        while (i < n - k - 1) {
            int left = i, right = i + k + 1, j = left + 1;
            while (j < right && days[j] > days[left] && days[j] > days[right]) j++;
            if (j == right) {
                ans = Math.min(ans, Math.max(days[left], days[right]));
                i++;
            } else i = j;
        }
        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
}
