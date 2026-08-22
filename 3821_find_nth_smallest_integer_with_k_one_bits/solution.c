// LeetCode 3821 - Find Nth Smallest Integer With K One Bits
// https://leetcode.com/problems/find-nth-smallest-integer-with-k-one-bits/

enum { MX3821 = 50 };

static long long c3821[MX3821][MX3821 + 1];
static int init3821 = 0;

static void ensure3821(void) {
    if (init3821) return;
    init3821 = 1;
    for (int i = 0; i < MX3821; i++) {
        c3821[i][0] = 1;
        for (int j = 1; j <= i; j++) c3821[i][j] = c3821[i - 1][j - 1] + c3821[i - 1][j];
    }
}

long long nthSmallest(long long n, int k) {
    ensure3821();
    long long ans = 0;
    for (int i = 49; i >= 0; i--) {
        if (n > c3821[i][k]) {
            n -= c3821[i][k];
            ans |= 1LL << i;
            k--;
            if (k == 0) break;
        }
    }
    return ans;
}
