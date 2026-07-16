// LeetCode 0410 - Split Array Largest Sum
export function splitArray(nums: number[], k: number): number {
    let left = Math.max(...nums);
    let right = nums.reduce((sum, value) => sum + value, 0);

    const canSplit = (limit: number): boolean => {
        let parts = 1;
        let current = 0;
        for (const value of nums) {
            if (current + value > limit) {
                parts += 1;
                current = 0;
            }
            current += value;
        }
        return parts <= k;
    };

    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (canSplit(mid)) right = mid;
        else left = mid + 1;
    }
    return left;
}
