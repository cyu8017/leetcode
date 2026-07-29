// LeetCode 1953 - Maximum Number of Weeks for Which You Can Work
// https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/

long long numberOfWeeks(int* milestones, int milestonesSize) {
    long long total = 0;
    int mx = 0;
    for (int i = 0; i < milestonesSize; i++) {
        total += milestones[i];
        if (milestones[i] > mx) mx = milestones[i];
    }
    long long rest = total - mx;
    if (mx > rest + 1) return 2 * rest + 1;
    return total;
}
