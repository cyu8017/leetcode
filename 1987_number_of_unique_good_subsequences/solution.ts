// LeetCode 1987 - Number of Unique Good Subsequences
// https://leetcode.com/problems/number-of-unique-good-subsequences/

function numberOfUniqueGoodSubsequences(binary: string): number {
    const MOD = 1000000007;
    let ends0 = 0, ends1 = 0, has0 = false;
    for (const ch of binary) {
        if (ch === "0") {
            has0 = true;
            ends0 = (ends0 + ends1) % MOD;
        } else {
            ends1 = (ends0 + ends1 + 1) % MOD;
        }
    }
    return (ends0 + ends1 + (has0 ? 1 : 0)) % MOD;
}
