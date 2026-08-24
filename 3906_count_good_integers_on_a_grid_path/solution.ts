// LeetCode 3906 - Count Good Integers On A Grid Path
// https://leetcode.com/problems/count-good-integers-on-a-grid-path/

export function countGoodIntegersOnPath(l: any, r: any, directions: any): any {
    const key = new Array(16).fill(false);
    let row = 0, col = 0;
    key[0] = true;
    for (const c of directions) {
        if (c === 'D') row++;
        else col++;
        key[row * 4 + col] = true;
    }
    let s = '', f;
    const dfs = (pos, last, lim) => {
        if (pos === 16) return 1;
        if (!lim && f[pos][last] !== -1) return f[pos][last];
        let res = 0;
        const start = key[pos] ? last : 0;
        const end = lim ? (s.charCodeAt(pos) - 48) : 9;
        for (let i = start; i <= end; i++) {
            const nextLast = key[pos] ? i : last;
            res += dfs(pos + 1, nextLast, lim && (i === end));
        }
        if (!lim) f[pos][last] = res;
        return res;
    };
    const calc = (x) => {
        if (x < 0) return 0;
        const t = String(x);
        s = '0'.repeat(16 - t.length) + t;
        f = Array.from({length: 16}, () => new Array(10).fill(-1));
        return dfs(0, 0, true);
    };
    return calc(r) - calc(l - 1);
}
