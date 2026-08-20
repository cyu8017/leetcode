// LeetCode 1397: Find All Good Strings

function findGoodStrings(n: any, s1: any, s2: any, evil: any): any {
    const mod = 1000000007, m = evil.length, lps = Array(m).fill(0);
    for (let i = 1, j = 0; i < m;) if (evil[i] === evil[j]) lps[i++] = ++j; else if (j) j = lps[j - 1]; else i++;
    const next = (matched: any, ch: any): any => { while (matched && evil[matched] !== ch) matched = lps[matched - 1]; return evil[matched] === ch ? matched + 1 : 0; };
    const count = (bound: any): any => {
        const memo = new Map();
        const dfs = (pos: any, matched: any, tight: any): any => {
            if (matched === m) return 0;
            if (pos === n) return 1;
            const key = `${pos},${matched},${tight}`;
            if (!tight && memo.has(key)) return memo.get(key);
            let result = 0, limit = tight ? bound.charCodeAt(pos) : 122;
            for (let code = 97; code <= limit; code++) result = (result + dfs(pos + 1, next(matched, String.fromCharCode(code)), tight && code === limit)) % mod;
            if (!tight) memo.set(key, result);
            return result;
        };
        return dfs(0, 0, true);
    };
    const decrement = (value: any): any => { const chars = value.split(""); for (let i = chars.length - 1; i >= 0; i--) { if (chars[i] > "a") { chars[i] = String.fromCharCode(chars[i].charCodeAt(0) - 1); return chars.join(""); } chars[i] = "z"; } return ""; };
    return (count(s2) - (s1 ? count(decrement(s1)) : 0) + mod) % mod;
}
