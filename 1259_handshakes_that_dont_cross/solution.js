// LeetCode 1259 - Handshakes That Don't Cross
// https://leetcode.com/problems/handshakes-that-dont-cross/

/**
 * @param {number} numPeople
 * @return {number}
 */
var numberOfWays = function(numPeople) {
    const mod = 1000000007;
    const dp = Array(numPeople + 1).fill(0);
    dp[0] = 1;
    for (let people = 2; people <= numPeople; people += 2) {
        let total = 0;
        for (let left = 0; left < people; left += 2) {
            total = (total + dp[left] * dp[people - 2 - left]) % mod;
        }
        dp[people] = total;
    }
    return dp[numPeople];
};
