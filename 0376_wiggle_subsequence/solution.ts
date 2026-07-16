export function wiggleMaxLength(nums: number[]): number {
    if (nums.length < 2) return nums.length;
    let up = 1;
    let down = 1;
    for (let index = 1; index < nums.length; index += 1) {
        if (nums[index] > nums[index - 1]) up = down + 1;
        else if (nums[index] < nums[index - 1]) down = up + 1;
    }
    return Math.max(up, down);
}
