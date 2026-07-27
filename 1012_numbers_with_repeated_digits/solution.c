// LeetCode 1012 - Numbers With Repeated Digits
// https://leetcode.com/problems/numbers-with-repeated-digits/

static int perm(int a, int b) {
    int res = 1;
    for (int i = 0; i < b; i++) res *= a - i;
    return res;
}

int numDupDigitsAtMostN(int n) {
    int digits[12], m = 0, x = n;
    while (x) {
        digits[m++] = x % 10;
        x /= 10;
    }
    for (int i = 0, j = m - 1; i < j; i++, j--) {
        int t = digits[i]; digits[i] = digits[j]; digits[j] = t;
    }
    int totalUnique = 0;
    for (int length = 1; length < m; length++)
        totalUnique += 9 * perm(9, length - 1);

    int used[10] = {0};
    int broken = 0;
    for (int i = 0; i < m; i++) {
        int d = digits[i];
        for (int v = (i == 0 ? 1 : 0); v < d; v++) {
            if (used[v]) continue;
            totalUnique += perm(9 - i, m - i - 1);
        }
        if (used[d]) { broken = 1; break; }
        used[d] = 1;
    }
    if (!broken) totalUnique += 1;
    return n - totalUnique;
}
