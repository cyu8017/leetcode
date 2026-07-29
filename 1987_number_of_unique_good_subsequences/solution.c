// LeetCode 1987 - Number of Unique Good Subsequences
// https://leetcode.com/problems/number-of-unique-good-subsequences/

int numberOfUniqueGoodSubsequences(char* binary) {
    const int MOD = 1000000007;
    long long ends0 = 0, ends1 = 0;
    int hasZero = 0;
    for (char* p = binary; *p; p++) {
        if (*p == '1') {
            ends1 = (ends1 + ends0 + 1) % MOD;
        } else {
            ends0 = (ends0 + ends1) % MOD;
            hasZero = 1;
        }
    }
    return (int)((ends0 + ends1 + hasZero) % MOD);
}
