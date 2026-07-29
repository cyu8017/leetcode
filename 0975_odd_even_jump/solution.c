// LeetCode 0975 - Odd Even Jump
// https://leetcode.com/problems/odd-even-jump/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef struct { int a, i; } Pair;
static int cmpAsc(const void* x, const void* y) {
    const Pair* p = x; const Pair* q = y;
    if (p->a != q->a) return p->a - q->a;
    return p->i - q->i;
}
static int cmpDesc(const void* x, const void* y) {
    const Pair* p = x; const Pair* q = y;
    if (p->a != q->a) return q->a - p->a;
    return p->i - q->i;
}

int oddEvenJumps(int* arr, int arrSize) {
    int n = arrSize;
    int* nextHigher = (int*)calloc((size_t)n, sizeof(int));
    int* nextLower = (int*)calloc((size_t)n, sizeof(int));
    Pair* pairs = (Pair*)malloc((size_t)n * sizeof(Pair));
    int* stack = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) { pairs[i].a = arr[i]; pairs[i].i = i; }
    qsort(pairs, (size_t)n, sizeof(Pair), cmpAsc);
    int top = 0;
    for (int t = 0; t < n; t++) {
        int i = pairs[t].i;
        while (top > 0 && stack[top - 1] < i) nextHigher[stack[--top]] = i;
        stack[top++] = i;
    }
    for (int i = 0; i < n; i++) { pairs[i].a = -arr[i]; pairs[i].i = i; }
    qsort(pairs, (size_t)n, sizeof(Pair), cmpAsc);
    top = 0;
    for (int t = 0; t < n; t++) {
        int i = pairs[t].i;
        while (top > 0 && stack[top - 1] < i) nextLower[stack[--top]] = i;
        stack[top++] = i;
    }
    bool* odd = (bool*)calloc((size_t)n, sizeof(bool));
    bool* even = (bool*)calloc((size_t)n, sizeof(bool));
    odd[n-1] = even[n-1] = true;
    for (int i = n - 2; i >= 0; i--) {
        if (nextHigher[i]) odd[i] = even[nextHigher[i]];
        if (nextLower[i]) even[i] = odd[nextLower[i]];
    }
    int ans = 0;
    for (int i = 0; i < n; i++) if (odd[i]) ans++;
    free(nextHigher); free(nextLower); free(pairs); free(stack); free(odd); free(even);
    return ans;
}
