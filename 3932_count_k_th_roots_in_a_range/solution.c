// LeetCode 3932 - Count K Th Roots In A Range
// https://leetcode.com/problems/count-k-th-roots-in-a-range/

int countKthRoots(int l, int r, int k) {
    if (k == 1) return r - l + 1;
    int ans = 0;
    for (int x = 0; ; x++) {
        long long y = 1;
        int overflow = 0;
        for (int i = 0; i < k; i++) {
            y *= x;
            if (y > r) { overflow = 1; break; }
        }
        if (overflow || y > r) break;
        if (l <= y && y <= r) ans++;
        if (x == 0 && k > 1) { /* 0^k = 0 */ }
        if (x > r) break;
    }
    return ans;
}
