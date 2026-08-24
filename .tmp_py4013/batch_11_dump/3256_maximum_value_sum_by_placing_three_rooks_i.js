// LeetCode 3256 - Maximum Value Sum by Placing Three Rooks I
// https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-i/

var maximumValueSum = function(board) {
    const m = board.length, n = board[0].length;
    const tops = [];
    for (let i = 0; i < m; i++) {
        const row = [];
        for (let j = 0; j < n; j++) {
            const cur = {v: board[i][j], c: j};
            let placed = false;
            for (let t = 0; t < row.length; t++) {
                if (cur.v > row[t].v) { row.splice(t, 0, cur); placed = true; break; }
            }
            if (!placed) row.push(cur);
            if (row.length > 3) row.length = 3;
        }
        tops.push(row);
    }
    let ans = Number.MIN_SAFE_INTEGER;
    for (let i = 0; i < m; i++) {
        for (const a of tops[i]) {
            for (let j = i + 1; j < m; j++) {
                for (const b of tops[j]) {
                    if (a.c === b.c) continue;
                    for (let k = j + 1; k < m; k++) {
                        for (const c of tops[k]) {
                            if (c.c === a.c || c.c === b.c) continue;
                            const s = a.v + b.v + c.v;
                            if (s > ans) ans = s;
                        }
                    }
                }
            }
        }
    }
    return ans;
};
