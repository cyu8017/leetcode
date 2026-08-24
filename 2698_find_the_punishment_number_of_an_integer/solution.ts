// LeetCode 2698 - Find the Punishment Number of an Integer
// https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

export function punishmentNumber(n: any): any {
    const dfs = (s, i, sum, target) => {
        if (i === s.length) return sum === target;
        let cur = 0;
        for (let j = i; j < s.length; j++) {
            cur = cur * 10 + (s.charCodeAt(j) - 48);
            if (sum + cur > target) break;
            if (dfs(s, j + 1, sum + cur, target)) return true;
        }
        return false;
    };
    let ans = 0;
    for (let i = 1; i <= n; i++) {
        const sq = i * i;
        if (dfs(String(sq), 0, 0, i)) ans += sq;
    }
    return ans;
}
