// LeetCode 0857 - Minimum Cost to Hire K Workers
// https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

#include <stdlib.h>

typedef struct { double ratio; int q; } Worker;

static int cmp_worker(const void* a, const void* b) {
    double d = ((const Worker*)a)->ratio - ((const Worker*)b)->ratio;
    return d < 0 ? -1 : (d > 0 ? 1 : 0);
}

double mincostToHireWorkers(int* quality, int qualitySize, int* wage, int wageSize, int k) {
    (void)wageSize;
    Worker* workers = (Worker*)malloc((size_t)qualitySize * sizeof(Worker));
    for (int i = 0; i < qualitySize; i++)
        workers[i] = (Worker){(double)wage[i] / quality[i], quality[i]};
    qsort(workers, (size_t)qualitySize, sizeof(Worker), cmp_worker);
    // max-heap of qualities
    int* heap = (int*)malloc((size_t)(k + 1) * sizeof(int));
    int hs = 0;
    long long total_q = 0;
    double ans = 1e300;
    for (int i = 0; i < qualitySize; i++) {
        int q = workers[i].q;
        // push -q as max heap via storing positive and comparing greater
        heap[hs] = q;
        // bubble up max
        int idx = hs++;
        while (idx > 0) {
            int p = (idx - 1) / 2;
            if (heap[p] >= heap[idx]) break;
            int t = heap[p]; heap[p] = heap[idx]; heap[idx] = t;
            idx = p;
        }
        total_q += q;
        if (hs > k) {
            // pop max
            total_q -= heap[0];
            heap[0] = heap[--hs];
            idx = 0;
            while (1) {
                int l = 2 * idx + 1, r = l + 1, largest = idx;
                if (l < hs && heap[l] > heap[largest]) largest = l;
                if (r < hs && heap[r] > heap[largest]) largest = r;
                if (largest == idx) break;
                int t = heap[idx]; heap[idx] = heap[largest]; heap[largest] = t;
                idx = largest;
            }
        }
        if (hs == k) {
            double cost = total_q * workers[i].ratio;
            if (cost < ans) ans = cost;
        }
    }
    free(workers); free(heap);
    return ans;
}
