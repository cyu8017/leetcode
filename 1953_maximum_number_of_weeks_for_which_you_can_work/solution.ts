// LeetCode 1953 - Maximum Number of Weeks for Which You Can Work
// https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/

function numberOfWeeks(milestones: number[]): number {
    const total = milestones.reduce((a, b: any) => a + b, 0);
    const mx = Math.max(...milestones);
    const rest = total - mx;
    if (mx > rest + 1) return 2 * rest + 1;
    return total;
}
