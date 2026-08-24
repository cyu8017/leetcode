// LeetCode 0639 - Decode Ways II
// https://leetcode.com/problems/decode-ways-ii/

export function numDecodings(s: string): number {
    const mod = 1000000007;
    const one = (ch) => {
        if (ch === "*") return 9;
        if (ch === "0") return 0;
        return 1;
    };
    const two = (a, b) => {
        if (a === "*" && b === "*") return 15;
        if (a === "*") return b <= "6" ? 2 : 1;
        if (b === "*") {
            if (a === "1") return 9;
            if (a === "2") return 6;
            return 0;
        }
        const value = (a.charCodeAt(0) - 48) * 10 + (b.charCodeAt(0) - 48);
        return value >= 10 && value <= 26 ? 1 : 0;
    };
    let prev2 = 1;
    let prev1 = one(s[0]);
    for (let i = 1; i < s.length; ++i) {
        const cur = (one(s[i]) * prev1 + two(s[i - 1], s[i]) * prev2) % mod;
        prev2 = prev1;
        prev1 = cur;
    }
    return prev1;
}
