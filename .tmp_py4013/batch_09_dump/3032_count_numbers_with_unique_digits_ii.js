// LeetCode 3032 - Count Numbers With Unique Digits II
// https://leetcode.com/problems/count-numbers-with-unique-digits-ii/

var numberCount = function(a, b) {
    let num = '';
    let f;
    function reset() {
        f = Array.from({length: num.length}, () => new Array(1 << 10).fill(-1));
    }
    function dfs(pos, mask, limit) {
        if (pos >= num.length) return mask !== 0 ? 1 : 0;
        if (!limit && f[pos][mask] !== -1) return f[pos][mask];
        const up = limit ? num.charCodeAt(pos) - 48 : 9;
        let ans = 0;
        for (let i = 0; i <= up; i++) {
            if (((mask >> i) & 1) !== 0) continue;
            let nxt = mask | (1 << i);
            if (mask === 0 && i === 0) nxt = 0;
            ans += dfs(pos + 1, nxt, limit && i === up);
        }
        if (!limit) f[pos][mask] = ans;
        return ans;
    }
    num = String(b);
    reset();
    const y = dfs(0, 0, true);
    num = String(a - 1);
    reset();
    const x = dfs(0, 0, true);
    return y - x;
};
