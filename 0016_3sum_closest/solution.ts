// LeetCode 0016 - 3Sum Closest
// https://leetcode.com/problems/3sum-closest/

export function threeSumClosest(nums: number[], target: number): number {
    nums.sort((a, b) => a - b);
    let closest = nums[0] + nums[1] + nums[2];

    for (let i = 0; i < nums.length - 2; i++) {
        let left = i + 1;
        let right = nums.length - 1;
        while (left < right) {
            const total = nums[i] + nums[left] + nums[right];
            if (Math.abs(total - target) < Math.abs(closest - target)) {
                closest = total;
            }
            if (total < target) {
                left++;
            } else if (total > target) {
                right--;
            } else {
                return total;
            }
        }
    }

    return closest;
}
