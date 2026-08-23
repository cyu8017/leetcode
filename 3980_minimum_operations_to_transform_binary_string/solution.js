// LeetCode 3980 - Minimum Operations to Transform Binary String
// https://leetcode.com/problems/minimum-operations-to-transform-binary-string/
var minOperations = function(s1, s2) {
        let infinity = 1000000000;
        let dp = [ 0, infinity ];
        let n = s1.length;
        for (let i = 0; i < n; i++) {
            let next = [ infinity, infinity ];
            for (let forcedZero = 0; forcedZero <= 1; forcedZero++) {
                if (dp[forcedZero] == infinity) continue;
                let current = s1[i];
                if (forcedZero == 1) current = '0';
                let direct = dp[forcedZero];
                if (current == '0' && s2[i] == '1') direct++;
                else if (current == '1' && s2[i] == '0') direct = infinity;
                next[0] = Math.min(next[0], direct);
                if (i + 1 < n) {
                    let cost = dp[forcedZero] + 1;
                    if (current == '0') cost++;
                    if (s1[i + 1] == '0') cost++;
                    if (s2[i] == '1') cost++;
                    next[1] = Math.min(next[1], cost);
                }
            }
            dp = next;
        }
        return dp[0] == infinity ? -1 : dp[0];
    
};
