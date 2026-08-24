// LeetCode 3981 - Count Distinct Ways to Form Target from Two Strings
// https://leetcode.com/problems/count-distinct-ways-to-form-target-from-two-strings/
var countWays = function(word1, word2, target) {
        let mod = 1000000007;
        let n1 = word1.length, n2 = word2.length;
        let size = (n1 + 1) * (n2 + 1) * 4;
        let dp = new Array(size).fill(0), next = new Array(size).fill(0);
        dp[index(0, 0, 0, n2)] = 1;
        for (let ti = 0; ti < target.length; ti++) {
            let ch = target[ti];
            next.fill(0);
            for (let j = 0; j <= n2; j++) {
                let prefix = new Array(4).fill(0);
                for (let a = 0; a < n1; a++) {
                    for (let mask = 0; mask < 4; mask++) {
                        prefix[mask] += dp[index(a, j, mask, n2)];
                        if (prefix[mask] >= mod) prefix[mask] -= mod;
                    }
                    if (word1[a] == ch) {
                        for (let mask = 0; mask < 4; mask++) {
                            let at = index(a + 1, j, mask | 1, n2);
                            next[at] += prefix[mask];
                            if (next[at] >= mod) next[at] -= mod;
                        }
                    }
                }
            }
            for (let i = 0; i <= n1; i++) {
                let prefix = new Array(4).fill(0);
                for (let b = 0; b < n2; b++) {
                    for (let mask = 0; mask < 4; mask++) {
                        prefix[mask] += dp[index(i, b, mask, n2)];
                        if (prefix[mask] >= mod) prefix[mask] -= mod;
                    }
                    if (word2[b] == ch) {
                        for (let mask = 0; mask < 4; mask++) {
                            let at = index(i, b + 1, mask | 2, n2);
                            next[at] += prefix[mask];
                            if (next[at] >= mod) next[at] -= mod;
                        }
                    }
                }
            }
            let tmp = dp; dp = next; next = tmp;
        }
        let answer = 0;
        for (let i = 0; i <= n1; i++) {
            for (let j = 0; j <= n2; j++) {
                answer += dp[index(i, j, 3, n2)];
                if (answer >= mod) answer -= mod;
            }
        }
        return answer;
    
};
var index = function(i, j, mask, n2) {
        return ((i * (n2 + 1) + j) * 4) + mask;
    
};
