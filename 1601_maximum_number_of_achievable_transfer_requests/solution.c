// LeetCode 1601 - Maximum Number of Achievable Transfer Requests
// https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

int maximumRequests(int n, int** requests, int requestsSize, int* requestsColSize) {
    (void)requestsColSize;
    int ans = 0;
    int total = 1 << requestsSize;
    for (int mask = 0; mask < total; mask++) {
        int bits = 0;
        for (int t = mask; t; t &= t - 1) bits++;
        if (bits <= ans) continue;
        int bal[20] = {0};
        for (int i = 0; i < requestsSize; i++) {
            if (mask & (1 << i)) {
                bal[requests[i][0]]--;
                bal[requests[i][1]]++;
            }
        }
        int ok = 1;
        for (int i = 0; i < n; i++) if (bal[i]) { ok = 0; break; }
        if (ok) ans = bits;
    }
    return ans;
}
