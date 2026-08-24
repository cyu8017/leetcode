// LeetCode 0805 - Split Array With Same Average
// https://leetcode.com/problems/split-array-with-same-average/

export function splitArraySameAverage(nums: number[]): boolean {
    const n = nums.length;
    let total = 0;
    for (const x of nums) total += x;
    nums.sort((a, b) => a - b);
    const memo = new Set();
    const find = (target, count, index) => {
        if (count === 0) return target === 0;
        if (index === n || count + index > n || target < 0) return false;
        const key = (target * 1048576) + (count * 1024) + index;
        if (memo.has(key)) return false;
        if (find(target - nums[index], count - 1, index + 1) || find(target, count, index + 1)) {
            return true;
        }
        memo.add(key);
        return false;
    };
    for (let size = 1; size < n; size++) {
        if ((total * size) % n === 0 && find(Math.floor(total * size / n), size, 0)) return true;
    }
    return false;
}
