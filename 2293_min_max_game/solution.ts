// LeetCode 2293 - Min Max Game
// https://leetcode.com/problems/min-max-game/

export function minMaxGame(nums: any): any {
    while (nums.length > 1) {
        const next = new Array(nums.length >> 1);
        for (let i = 0; i < next.length; i++) {
            if (i % 2 === 0) next[i] = Math.min(nums[2 * i], nums[2 * i + 1]);
            else next[i] = Math.max(nums[2 * i], nums[2 * i + 1]);
        }
        nums = next;
    }
    return nums[0];
}
