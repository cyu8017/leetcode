// LeetCode 0416 - Partition Equal Subset Sum
export function canPartition(nums: number[]): boolean {
    const total = nums.reduce((sum, value) => sum + value, 0);
    if (total % 2) return false;
    const target = total / 2;
    let possible = new Set<number>([0]);
    for (const value of nums) {
        possible = new Set([...possible, ...[...possible].map((amount) => amount + value).filter((amount) => amount <= target)]);
        if (possible.has(target)) return true;
    }
    return possible.has(target);
}
