// LeetCode 1018 - Binary Prefix Divisible By 5
// https://leetcode.com/problems/binary-prefix-divisible-by-5/

function prefixesDivBy5(nums: number[]): boolean[] {
    const ans = [];
    let rem = 0;
    for (const bit of nums) {
        rem = (rem * 2 + bit) % 5;
        ans.push(rem === 0);
    }
    return ans;
}
