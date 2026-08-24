// LeetCode 2562 - Find the Array Concatenation Value
// https://leetcode.com/problems/find-the-array-concatenation-value/

export function findTheArrayConcVal(nums: number[]): number {
    let ans = 0, l = 0, r = nums.length - 1;
    while (l <= r) {
        if (l === r) {
            ans += nums[l];
            break;
        }
        const left = nums[l], right = nums[r];
        let pow = 1;
        for (let t = right; t > 0; t = Math.floor(t / 10)) pow *= 10;
        ans += left * pow + right;
        l++;
        r--;
    }
    return ans;
}
