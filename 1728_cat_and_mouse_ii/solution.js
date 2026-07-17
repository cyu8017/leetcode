// LeetCode 1728 - Cat and Mouse II
// https://leetcode.com/problems/cat-and-mouse-ii/

/**
 * @param {string[]} grid
 * @param {number} catJump
 * @param {number} mouseJump
 * @return {boolean}
 */
var canMouseWin = function(grid, catJump, mouseJump) {
    const rows = grid.length;
    const cols = grid[0].length;
    let totalOpen = 0;
    let mouse = 0;
    let cat = 0;
    let food = 0;
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            const cell = grid[r][c];
            if (cell !== '#') totalOpen++;
            if (cell === 'M') mouse = r * cols + c;
            else if (cell === 'C') cat = r * cols + c;
            else if (cell === 'F') food = r * cols + c;
        }
    }
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    const computeMoves = (pos, jump) => {
        const r = Math.floor(pos / cols);
        const c = pos % cols;
        const out = [pos];
        for (const [dr, dc] of dirs) {
            for (let step = 1; step <= jump; step++) {
                const nr = r + dr * step;
                const nc = c + dc * step;
                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || grid[nr][nc] === '#') break;
                out.push(nr * cols + nc);
            }
        }
        return out;
    };
    const cells = rows * cols;
    const mouseMoves = new Array(cells);
    const catMoves = new Array(cells);
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (grid[r][c] !== '#') {
                const pos = r * cols + c;
                mouseMoves[pos] = computeMoves(pos, mouseJump);
                catMoves[pos] = computeMoves(pos, catJump);
            }
        }
    }
    const maxTurn = 2 * totalOpen;
    const memo = new Int8Array(cells * cells * maxTurn);
    const win = (m, c, turn) => {
        if (turn >= maxTurn) return false;
        if (m === food) return true;
        if (c === food || c === m) return false;
        const key = (m * cells + c) * maxTurn + turn;
        if (memo[key] !== 0) return memo[key] === 1;
        let result;
        if (turn % 2 === 0) {
            result = mouseMoves[m].some((nm) => win(nm, c, turn + 1));
        } else {
            result = catMoves[c].every((nc) => win(m, nc, turn + 1));
        }
        memo[key] = result ? 1 : 2;
        return result;
    };
    return win(mouse, cat, 0);
};
