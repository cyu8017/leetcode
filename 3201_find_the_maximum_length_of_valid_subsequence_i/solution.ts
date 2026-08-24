// LeetCode 3201 - Find the Maximum Length of Valid Subsequence I
// https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/

export function maximumLength(nums: any): any {
    const k = 2;
    const f = Array.from({length: k}, () => new Array(k).fill(0));
    let ans = 0;
    for (const raw of nums) {
        const x = raw % k;
        for (let j = 0; j < k; j++) {
            const y = (j - x + k) % k;
            f[x][y] = f[y][x] + 1;
            ans = Math.max(ans, f[x][y]);
        }
    }
    return ans;
}
