// LeetCode 3762 - Minimum Operations to Equalize Subarrays
// https://leetcode.com/problems/minimum-operations-to-equalize-subarrays/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int left, right, count;
    long long sum;
} Node;

static Node* nodes;
static int nodesN, nodesCap;

static int imin(int a, int b) { return a < b ? a : b; }
static int imax(int a, int b) { return a > b ? a : b; }

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

static int lowerBound(int* a, int n, int x) {
    int lo = 0, hi = n;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (a[mid] < x) lo = mid + 1; else hi = mid;
    }
    return lo;
}

static int update(int previous, int lo, int hi, int position, int value) {
    if (nodesN == nodesCap) {
        nodesCap = nodesCap ? nodesCap * 2 : 64;
        nodes = (Node*)realloc(nodes, (size_t)nodesCap * sizeof(Node));
    }
    int current = nodesN++;
    nodes[current] = nodes[previous];
    nodes[current].count++;
    nodes[current].sum += value;
    if (lo < hi) {
        int mid = (lo + hi) / 2;
        if (position <= mid)
            nodes[current].left = update(nodes[previous].left, lo, mid, position, value);
        else
            nodes[current].right = update(nodes[previous].right, mid + 1, hi, position, value);
    }
    return current;
}

static int kth(int rightRoot, int leftRoot, int lo, int hi, int rank) {
    if (lo == hi) return lo;
    int leftCount = nodes[nodes[rightRoot].left].count - nodes[nodes[leftRoot].left].count;
    int mid = (lo + hi) / 2;
    if (rank <= leftCount)
        return kth(nodes[rightRoot].left, nodes[leftRoot].left, lo, mid, rank);
    return kth(nodes[rightRoot].right, nodes[leftRoot].right, mid + 1, hi, rank - leftCount);
}

static void prefixStats(int rightRoot, int leftRoot, int lo, int hi, int end, int* count, long long* sum) {
    if (end < lo) { *count = 0; *sum = 0; return; }
    if (hi <= end) {
        *count = nodes[rightRoot].count - nodes[leftRoot].count;
        *sum = nodes[rightRoot].sum - nodes[leftRoot].sum;
        return;
    }
    int mid = (lo + hi) / 2;
    int c1; long long s1;
    prefixStats(nodes[rightRoot].left, nodes[leftRoot].left, lo, mid, end, &c1, &s1);
    if (end > mid) {
        int c2; long long s2;
        prefixStats(nodes[rightRoot].right, nodes[leftRoot].right, mid + 1, hi, end, &c2, &s2);
        c1 += c2; s1 += s2;
    }
    *count = c1; *sum = s1;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* minOperations(int* nums, int numsSize, int k, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int n = numsSize;
    int* quotient = (int*)malloc((size_t)n * sizeof(int));
    int* remainder = (int*)malloc((size_t)n * sizeof(int));
    int* values = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) {
        quotient[i] = nums[i] / k;
        remainder[i] = nums[i] % k;
        values[i] = quotient[i];
    }
    qsort(values, (size_t)n, sizeof(int), cmpInt);
    int* unique = (int*)malloc((size_t)n * sizeof(int));
    int un = 0;
    for (int i = 0; i < n; i++) {
        if (un == 0 || unique[un - 1] != values[i]) unique[un++] = values[i];
    }
    nodesCap = 64; nodesN = 1;
    nodes = (Node*)calloc((size_t)nodesCap, sizeof(Node));
    int* roots = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 0; i < n; i++) {
        int position = lowerBound(unique, un, quotient[i]);
        roots[i + 1] = update(roots[i], 0, un - 1, position, quotient[i]);
    }
    int* logt = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 2; i <= n; i++) logt[i] = logt[i / 2] + 1;
    int levels = logt[n] + 1;
    int** minTable = (int**)malloc((size_t)levels * sizeof(int*));
    int** maxTable = (int**)malloc((size_t)levels * sizeof(int*));
    minTable[0] = (int*)malloc((size_t)n * sizeof(int));
    maxTable[0] = (int*)malloc((size_t)n * sizeof(int));
    memcpy(minTable[0], remainder, (size_t)n * sizeof(int));
    memcpy(maxTable[0], remainder, (size_t)n * sizeof(int));
    for (int level = 1; level < levels; level++) {
        int length = n - (1 << level) + 1;
        minTable[level] = (int*)malloc((size_t)length * sizeof(int));
        maxTable[level] = (int*)malloc((size_t)length * sizeof(int));
        int half = 1 << (level - 1);
        for (int i = 0; i < length; i++) {
            minTable[level][i] = imin(minTable[level - 1][i], minTable[level - 1][i + half]);
            maxTable[level][i] = imax(maxTable[level - 1][i], maxTable[level - 1][i + half]);
        }
    }
    long long* answer = (long long*)malloc((size_t)queriesSize * sizeof(long long));
    for (int qi = 0; qi < queriesSize; qi++) {
        int left = queries[qi][0], right = queries[qi][1];
        int length = right - left + 1;
        int level = logt[length];
        int offset = right - (1 << level) + 1;
        int minR = imin(minTable[level][left], minTable[level][offset]);
        int maxR = imax(maxTable[level][left], maxTable[level][offset]);
        if (minR != maxR) { answer[qi] = -1; continue; }
        int medianIndex = kth(roots[right + 1], roots[left], 0, un - 1, (length + 1) / 2);
        int median = unique[medianIndex];
        int leftCount; long long leftSum;
        prefixStats(roots[right + 1], roots[left], 0, un - 1, medianIndex, &leftCount, &leftSum);
        long long totalSum = nodes[roots[right + 1]].sum - nodes[roots[left]].sum;
        answer[qi] = (long long)median * leftCount - leftSum + (totalSum - leftSum) - (long long)median * (length - leftCount);
    }
    for (int level = 0; level < levels; level++) { free(minTable[level]); free(maxTable[level]); }
    free(minTable); free(maxTable); free(quotient); free(remainder); free(values); free(unique); free(roots); free(logt); free(nodes);
    *returnSize = queriesSize;
    return answer;
}
