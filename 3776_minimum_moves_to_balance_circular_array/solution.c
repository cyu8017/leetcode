// LeetCode 3776 - Minimum Moves To Balance Circular Array
// https://leetcode.com/problems/minimum-moves-to-balance-circular-array/

long long minMoves(int* balance, int balanceSize) {
    long long sum = 0;
    for (int i = 0; i < balanceSize; i++) sum += balance[i];
    if (sum < 0) return -1;
    int n = balanceSize;
    int mn = balance[0], idx = 0;
    for (int i = 1; i < n; i++) {
        if (balance[i] < mn) { mn = balance[i]; idx = i; }
    }
    if (mn >= 0) return 0;
    int need = -mn;
    long long ans = 0;
    for (int j = 1; j < n; j++) {
        int a = balance[(idx - j + n) % n];
        int b = balance[(idx + j) % n];
        int c1 = a < need ? a : need;
        need -= c1;
        ans += (long long)c1 * j;
        int c2 = b < need ? b : need;
        need -= c2;
        ans += (long long)c2 * j;
    }
    return ans;
}
