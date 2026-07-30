// LeetCode 1953 - Maximum Number of Weeks for Which You Can Work
// https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/

using System.Linq;

public class Solution {
    public long NumberOfWeeks(int[] milestones) {
        long total = milestones.Sum(x => (long)x);
        long mx = milestones.Max();
        long rest = total - mx;
        if (mx > rest + 1) return 2 * rest + 1;
        return total;
    }
}