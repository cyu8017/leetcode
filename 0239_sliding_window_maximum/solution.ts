// LeetCode 0239 - Sliding Window Maximum
// https://leetcode.com/problems/sliding-window-maximum/

export function maxSlidingWindow(nums: number[], k: number): number[] {
    const window: number[] = [];
    const result: number[] = [];

    for (let index = 0; index < nums.length; index++) {
        while (window.length > 0 && nums[window[window.length - 1]] <= nums[index]) {
            window.pop();
        }
        window.push(index);
        if (window[0] <= index - k) {
            window.shift();
        }
        if (index >= k - 1) {
            result.push(nums[window[0]]);
        }
    }

    return result;
}
