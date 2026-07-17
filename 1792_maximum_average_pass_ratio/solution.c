// LeetCode 1792 - Maximum Average Pass Ratio
// https://leetcode.com/problems/maximum-average-pass-ratio/

#include <stdlib.h>

typedef struct {
    double gain;
    double p;
    double t;
} Entry;

static double computeGain(double p, double t) {
    return (p + 1) / (t + 1) - p / t;
}

static void siftDown(Entry* heap, int n, int i) {
    while (1) {
        int largest = i;
        int l = 2 * i + 1;
        int r = 2 * i + 2;
        if (l < n && heap[l].gain > heap[largest].gain) largest = l;
        if (r < n && heap[r].gain > heap[largest].gain) largest = r;
        if (largest == i) break;
        Entry tmp = heap[i];
        heap[i] = heap[largest];
        heap[largest] = tmp;
        i = largest;
    }
}

double maxAverageRatio(int** classes, int classesSize, int* classesColSize, int extraStudents) {
    Entry* heap = (Entry*)malloc(classesSize * sizeof(Entry));
    for (int i = 0; i < classesSize; i++) {
        double p = classes[i][0];
        double t = classes[i][1];
        heap[i].gain = computeGain(p, t);
        heap[i].p = p;
        heap[i].t = t;
    }
    for (int i = classesSize / 2 - 1; i >= 0; i--) {
        siftDown(heap, classesSize, i);
    }
    for (int k = 0; k < extraStudents; k++) {
        double p = heap[0].p + 1;
        double t = heap[0].t + 1;
        heap[0].gain = computeGain(p, t);
        heap[0].p = p;
        heap[0].t = t;
        siftDown(heap, classesSize, 0);
    }
    double total = 0;
    for (int i = 0; i < classesSize; i++) {
        total += heap[i].p / heap[i].t;
    }
    free(heap);
    return total / classesSize;
}
