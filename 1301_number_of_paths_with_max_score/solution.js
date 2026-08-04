// LeetCode 1301 - Number Of Paths With Max Score
// https://leetcode.com/problems/number-of-paths-with-max-score/

/**
 * @param {string[]} board
 * @return {number[]}
 */
var pathsWithMaxScore = function(board) {
    const mod = 1000000007;
    const n = board.length;
    const score = Array.from({ length: n }, () => Array(n).fill(-1));
    const ways = Array.from({ length: n }, () => Array(n).fill(0));
    score[n - 1][n - 1] = 0;
    ways[n - 1][n - 1] = 1;
    for (let r = n - 1; r >= 0; r--) {
        for (let c = n - 1; c >= 0; c--) {
            if (board[r][c] === "X" || (r === n - 1 && c === n - 1)) continue;
            let best = -1, count = 0;
            for (const [nr, nc] of [[r + 1, c], [r, c + 1], [r + 1, c + 1]]) {
                if (nr < n && nc < n && score[nr][nc] >= 0) {
                    if (score[nr][nc] > best) {
                        best = score[nr][nc];
                        count = ways[nr][nc];
                    } else if (score[nr][nc] === best) {
                        count = (count + ways[nr][nc]) % mod;
                    }
                }
            }
            if (best >= 0) {
                const ch = board[r][c];
                score[r][c] = best + (ch >= "0" && ch <= "9" ? Number(ch) : 0);
                ways[r][c] = count;
            }
        }
    }
    return [Math.max(score[0][0], 0), ways[0][0]];
};
