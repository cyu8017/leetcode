// LeetCode 3200 - Maximum Height of a Triangle
// https://leetcode.com/problems/maximum-height-of-a-triangle/

export function maxHeightOfTriangle(red: any, blue: any): any {
    let ans = 0;
    for (let k = 0; k < 2; k++) {
        const c = [red, blue];
        for (let i = 1, j = k; i <= c[j]; i++, j ^= 1) {
            c[j] -= i;
            ans = Math.max(ans, i);
        }
    }
    return ans;
}
