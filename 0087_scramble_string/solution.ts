// LeetCode 0087 - Scramble String
// https://leetcode.com/problems/scramble-string/

export function isScramble(s1: string, s2: string): boolean {
    const memo = new Map<string, boolean>();

    function dfs(a: string, b: string): boolean {
        const key = a + '#' + b;
        if (memo.has(key)) {
            return memo.get(key)!;
        }
        if (a === b) {
            memo.set(key, true);
            return true;
        }
        if ([...a].sort().join('') !== [...b].sort().join('')) {
            memo.set(key, false);
            return false;
        }

        const n = a.length;
        for (let i = 1; i < n; i++) {
            if (dfs(a.slice(0, i), b.slice(0, i)) && dfs(a.slice(i), b.slice(i))) {
                memo.set(key, true);
                return true;
            }
            if (dfs(a.slice(0, i), b.slice(n - i)) && dfs(a.slice(i), b.slice(0, n - i))) {
                memo.set(key, true);
                return true;
            }
        }
        memo.set(key, false);
        return false;
    }

    return dfs(s1, s2);
}
