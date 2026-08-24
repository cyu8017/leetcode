// LeetCode 2282 - Number of People That Can Be Seen in a Grid
// https://leetcode.com/problems/number-of-people-that-can-be-seen-in-a-grid/

export function seePeople(heights: any): any {
    const m = heights.length, n = heights[0].length;
    const ans = Array.from({length: m}, () => new Array(n).fill(0));
    for (let i = 0; i < m; i++) {
        const stack = [];
        for (let j = n - 1; j >= 0; j--) {
            let cnt = 0;
            while (stack.length && heights[i][stack[stack.length - 1]] < heights[i][j]) {
                stack.pop(); cnt++;
            }
            if (stack.length) cnt++;
            ans[i][j] += cnt;
            while (stack.length && heights[i][stack[stack.length - 1]] === heights[i][j]) stack.pop();
            stack.push(j);
        }
    }
    for (let j = 0; j < n; j++) {
        const stack = [];
        for (let i = m - 1; i >= 0; i--) {
            let cnt = 0;
            while (stack.length && heights[stack[stack.length - 1]][j] < heights[i][j]) {
                stack.pop(); cnt++;
            }
            if (stack.length) cnt++;
            ans[i][j] += cnt;
            while (stack.length && heights[stack[stack.length - 1]][j] === heights[i][j]) stack.pop();
            stack.push(i);
        }
    }
    return ans;
}
