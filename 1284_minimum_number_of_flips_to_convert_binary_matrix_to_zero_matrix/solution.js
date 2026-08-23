// LeetCode 1284 - Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
// https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

/**
 * @param {number[][]} mat
 * @return {number}
 */
var minFlips = function(mat) {
    const m = mat.length;
    const n = mat[0].length;
    let start = 0;
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (mat[r][c]) start |= 1 << (r * n + c);
        }
    }
    const deltas = [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]];
    const masks = [];
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            let mask = 0;
            for (const [dr, dc] of deltas) {
                const nr = r + dr;
                const nc = c + dc;
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    mask ^= 1 << (nr * n + nc);
                }
            }
            masks.push(mask);
        }
    }
    const queue = [[start, 0]];
    const seen = new Set([start]);
    while (queue.length) {
        const [state, distance] = queue.shift();
        if (state === 0) return distance;
        for (const mask of masks) {
            const nxt = state ^ mask;
            if (!seen.has(nxt)) {
                seen.add(nxt);
                queue.push([nxt, distance + 1]);
            }
        }
    }
    return -1;
};
