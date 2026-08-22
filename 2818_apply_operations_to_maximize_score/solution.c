// LeetCode 2818 - Apply Operations to Maximize Score
// https://leetcode.com/problems/apply-operations-to-maximize-score/

#include <stdlib.h>
#include <stdbool.h>

typedef struct { int v; long long cnt; } Pair2818;
static int cmp_p2818(const void* a, const void* b) {
    return ((const Pair2818*)b)->v - ((const Pair2818*)a)->v;
}
static long long modPow(long long a, long long b) {
    const int mod = 1000000007;
    long long res = 1;
    a %= mod;
    while (b > 0) {
        if (b & 1) res = res * a % mod;
        a = a * a % mod;
        b >>= 1;
    }
    return res;
}

int maximumScore(int* nums, int numsSize, int k) {
    const int mod = 1000000007;
    int n = numsSize;
    int maxV = 0;
    for (int i = 0; i < n; i++) if (nums[i] > maxV) maxV = nums[i];
    int* spf = (int*)calloc(maxV + 1, sizeof(int));
    for (int i = 2; i <= maxV; i++) {
        if (spf[i] == 0) {
            for (int j = i; j <= maxV; j += i)
                if (spf[j] == 0) spf[j] = i;
        }
    }
    int* score = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        int x = nums[i], cnt = 0, last = -1;
        while (x > 1) {
            int p = spf[x];
            if (p != last) { cnt++; last = p; }
            x /= p;
        }
        score[i] = cnt;
    }
    int* left = (int*)malloc(n * sizeof(int));
    int* right = (int*)malloc(n * sizeof(int));
    int* st = (int*)malloc(n * sizeof(int));
    int top = 0;
    for (int i = 0; i < n; i++) {
        while (top > 0 && score[st[top - 1]] < score[i]) top--;
        left[i] = top == 0 ? -1 : st[top - 1];
        st[top++] = i;
    }
    top = 0;
    for (int i = n - 1; i >= 0; i--) {
        while (top > 0 && score[st[top - 1]] <= score[i]) top--;
        right[i] = top == 0 ? n : st[top - 1];
        st[top++] = i;
    }
    Pair2818* arr = (Pair2818*)malloc(n * sizeof(Pair2818));
    for (int i = 0; i < n; i++) {
        arr[i].v = nums[i];
        arr[i].cnt = (long long)(i - left[i]) * (right[i] - i);
    }
    qsort(arr, n, sizeof(Pair2818), cmp_p2818);
    long long ans = 1;
    long long remain = k;
    for (int i = 0; i < n && remain > 0; i++) {
        long long use = arr[i].cnt;
        if (use > remain) use = remain;
        ans = ans * modPow(arr[i].v, use) % mod;
        remain -= use;
    }
    free(spf); free(score); free(left); free(right); free(st); free(arr);
    return (int)ans;
}
