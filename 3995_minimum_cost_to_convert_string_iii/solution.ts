// LeetCode 3995 - Minimum Cost to Convert String III
// https://leetcode.com/problems/minimum-cost-to-convert-string-iii/

export function minCost(source: any, target: any, rules: any, costs: any): any {
        let n = source.length;
        if (target.length != n) return -1;
        let dp = new Array(n + 1).fill(0);
        for (let i = 0; i <= n; i++) dp[i] = 2147483647;
        dp[0] = 0;
        for (let i = 0; i < n; i++) {
            if (dp[i] == 2147483647) continue;
            if (source[i] == target[i] && dp[i] < dp[i + 1]) dp[i + 1] = dp[i];
            for (let j = 0; j < rules.length; j++) {
                let p = rules[j][0];
                let r = rules[j][1];
                let plen = p.length;
                if (i + plen > n) continue;
                let c = costs[j];
                let ok = true;
                for (let k = 0; k < plen; k++) {
                    if (r[k] != target[i + k]) { ok = false; break; }
                    if (p[k] == '*') ++c;
                    else if (p[k] != source[i + k]) { ok = false; break; }
                }
                if (ok && dp[i] <= 2147483647 - c && dp[i] + c < dp[i + plen]) {
                    dp[i + plen] = dp[i] + c;
                }
            }
        }
        return dp[n] == 2147483647 ? -1 : dp[n];
    
}
