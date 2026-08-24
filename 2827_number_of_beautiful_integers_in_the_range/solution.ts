// LeetCode 2827 - Number of Beautiful Integers in the Range
// https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/

export function numberOfBeautifulIntegers(low: number, high: number, k: number): number {
    const count = (n) => {
        if (n < 0) return 0;
        const s = String(n);
        const memo = Array.from({length: 12}, () =>
            Array.from({length: 45}, () =>
                Array.from({length: 22}, () =>
                    Array.from({length: 2}, () => Array(2).fill(-1)))));
        const dfs = (pos, diff, mod, tight, started) => {
            if (pos === s.length) return (started && diff === 0 && mod === 0) ? 1 : 0;
            if (memo[pos][diff + 20][mod][tight][started] !== -1)
                return memo[pos][diff + 20][mod][tight][started];
            const up = tight ? s.charCodeAt(pos) - 48 : 9;
            let ans = 0;
            for (let digit = 0; digit <= up; digit++) {
                const nt = tight && digit === up ? 1 : 0;
                if (!started) {
                    if (digit === 0) ans += dfs(pos + 1, diff, mod, nt, 0);
                    else {
                        const nd = diff + (digit % 2 === 0 ? 1 : -1);
                        ans += dfs(pos + 1, nd, digit % k, nt, 1);
                    }
                } else {
                    const nd = diff + (digit % 2 === 0 ? 1 : -1);
                    ans += dfs(pos + 1, nd, (mod * 10 + digit) % k, nt, 1);
                }
            }
            return memo[pos][diff + 20][mod][tight][started] = ans;
        };
        return dfs(0, 0, 0, 1, 0);
    };
    return count(high) - count(low - 1);
}
