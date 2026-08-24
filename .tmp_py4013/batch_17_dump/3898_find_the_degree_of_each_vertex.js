// LeetCode 3898 - Find The Degree Of Each Vertex
// https://leetcode.com/problems/find-the-degree-of-each-vertex/

var findDegrees = function(matrix) {
    const ans = new Array(matrix.length).fill(0);
    for (let i = 0; i < matrix.length; i++) {
        for (const x of matrix[i]) ans[i] += x;
    }
    return ans;
};
