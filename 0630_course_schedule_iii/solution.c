// LeetCode 0630 - Course Schedule III
// https://leetcode.com/problems/course-schedule-iii/

#include <stdlib.h>

static int cmpByDeadline(const void* a, const void* b) {
    const int* left = *(const int* const*)a;
    const int* right = *(const int* const*)b;
    return left[1] - right[1];
}

static void heapPush(int* heap, int* size, int value) {
    int i = (*size)++;
    heap[i] = value;
    while (i > 0) {
        int parent = (i - 1) / 2;
        if (heap[parent] >= heap[i]) {
            break;
        }
        int tmp = heap[parent];
        heap[parent] = heap[i];
        heap[i] = tmp;
        i = parent;
    }
}

static int heapPop(int* heap, int* size) {
    int top = heap[0];
    heap[0] = heap[--(*size)];
    int i = 0;
    while (1) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        if (left < *size && heap[left] > heap[largest]) {
            largest = left;
        }
        if (right < *size && heap[right] > heap[largest]) {
            largest = right;
        }
        if (largest == i) {
            break;
        }
        int tmp = heap[i];
        heap[i] = heap[largest];
        heap[largest] = tmp;
        i = largest;
    }
    return top;
}

int scheduleCourse(int** courses, int coursesSize, int* coursesColSize) {
    (void)coursesColSize;
    qsort(courses, (size_t)coursesSize, sizeof(int*), cmpByDeadline);
    int* heap = (int*)malloc((size_t)coursesSize * sizeof(int));
    int heapSize = 0;
    int time = 0;
    for (int i = 0; i < coursesSize; i++) {
        int duration = courses[i][0];
        int lastDay = courses[i][1];
        if (time + duration <= lastDay) {
            heapPush(heap, &heapSize, duration);
            time += duration;
        } else if (heapSize > 0 && heap[0] > duration) {
            time += duration - heapPop(heap, &heapSize);
            heapPush(heap, &heapSize, duration);
        }
    }
    int answer = heapSize;
    free(heap);
    return answer;
}
