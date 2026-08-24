// LeetCode 3678 - Smallest Absent Positive Greater Than Average
// https://leetcode.com/problems/smallest-absent-positive-greater-than-average/

export function smallestAbsent(nums: any): any {
    const s = new Set();
    let sum = 0;
    for (const x of nums) {
        s.add(x);
        sum += x;
    }
    let ans = Math.max(1, Math.floor(sum / nums.length) + 1);
    while (s.has(ans)) ans++;
    return ans;
}
