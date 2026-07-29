// LeetCode 0668 - Kth Smallest Number in Multiplication Table
// https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

int findKthNumber(int m, int n, int k) {
    int lo = 1, hi = m * n;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        int count = 0;
        for (int i = 1; i <= m; i++) {
            int add = mid / i;
            count += add < n ? add : n;
        }
        if (count < k) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}
