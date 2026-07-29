// LeetCode 0940 - Distinct Subsequences II
// https://leetcode.com/problems/distinct-subsequences-ii/

int distinctSubseqII(char* s) {
    const int MOD = 1000000007;
    long long ends[26] = {0};
    long long total = 1;
    for (; *s; s++) {
        int c = *s - 'a';
        long long prev = ends[c];
        ends[c] = total;
        total = (total - prev + ends[c] + MOD) % MOD;
    }
    return (int)((total - 1 + MOD) % MOD);
}
