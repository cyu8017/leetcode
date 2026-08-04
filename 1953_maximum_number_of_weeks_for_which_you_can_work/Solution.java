// LeetCode 1953 - Maximum Number of Weeks for Which You Can Work
// https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/

class Solution {
    public long numberOfWeeks(int[] milestones) {
        long total = 0, mx = 0;
        for (int x : milestones) {
            total += x;
            mx = Math.max(mx, x);
        }
        long rest = total - mx;
        if (mx > rest + 1) return 2 * rest + 1;
        return total;
    }
}
