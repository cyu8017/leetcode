// LeetCode 3086 - Minimum Moves to Pick K Ones
// https://leetcode.com/problems/minimum-moves-to-pick-k-ones/

#include <stdlib.h>
#include <limits.h>

static int imin(int a, int b) { return a < b ? a : b; }
static int imax(int a, int b) { return a > b ? a : b; }

long long minimumMoves(int* nums, int numsSize, int k, int maxChanges) {
    int n = numsSize;
    int* cnt = (int*)calloc((size_t)(n + 1), sizeof(int));
    long long* s = (long long*)calloc((size_t)(n + 1), sizeof(long long));
    for (int i = 1; i <= n; i++) {
        cnt[i] = cnt[i - 1] + nums[i - 1];
        s[i] = s[i - 1] + (long long)i * nums[i - 1];
    }
    long long ans = LLONG_MAX;
    for (int i = 1; i <= n; i++) {
        int t = 0;
        int need = k - nums[i - 1];
        int neigh[2] = {i - 1, i + 1};
        for (int ni = 0; ni < 2; ni++) {
            int j = neigh[ni];
            if (need > 0 && 1 <= j && j <= n && nums[j - 1] == 1) { need--; t++; }
        }
        int c = imin(need, maxChanges);
        need -= c;
        t += c * 2;
        if (need <= 0) {
            if (t < ans) ans = t;
            continue;
        }
        int l = 2, r = imax(i - 1, n - i);
        while (l <= r) {
            int mid = (l + r) >> 1;
            int l1 = imax(1, i - mid), r1 = imax(0, i - 2);
            int l2 = imin(n + 1, i + 2), r2 = imin(n, i + mid);
            int c1 = cnt[r1] - cnt[l1 - 1];
            int c2 = cnt[r2] - cnt[l2 - 1];
            if (c1 + c2 >= need) {
                long long t1 = (long long)c1 * i - (s[r1] - s[l1 - 1]);
                long long t2 = s[r2] - s[l2 - 1] - (long long)c2 * i;
                if (t + t1 + t2 < ans) ans = t + t1 + t2;
                r = mid - 1;
            } else l = mid + 1;
        }
    }
    free(cnt); free(s);
    return ans;
}
