// LeetCode 2672 - Number of Adjacent Elements With the Same Color
// https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

var colorTheArray = function(n, queries) {
    const colors = new Array(n).fill(0);
    const ans = new Array(queries.length);
    let same = 0;
    for (let i = 0; i < queries.length; i++) {
        const idx = queries[i][0], color = queries[i][1];
        if (colors[idx] !== 0) {
            if (idx > 0 && colors[idx] === colors[idx - 1]) same--;
            if (idx + 1 < n && colors[idx] === colors[idx + 1]) same--;
        }
        colors[idx] = color;
        if (idx > 0 && colors[idx] === colors[idx - 1]) same++;
        if (idx + 1 < n && colors[idx] === colors[idx + 1]) same++;
        ans[i] = same;
    }
    return ans;
};
