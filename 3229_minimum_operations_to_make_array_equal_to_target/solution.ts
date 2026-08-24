// LeetCode 3229 - Minimum Operations to Make Array Equal to Target
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/

export function minimumOperations(nums: any, target: any): any {
    let f = Math.abs(target[0] - nums[0]);
    for (let i = 1; i < target.length; i++) {
        const x = target[i] - nums[i];
        const y = target[i - 1] - nums[i - 1];
        if (x * y > 0) {
            const d = Math.abs(x) - Math.abs(y);
            if (d > 0) f += d;
        } else {
            f += Math.abs(x);
        }
    }
    return f;
}
