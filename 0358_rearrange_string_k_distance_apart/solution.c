// LeetCode 0358 - Rearrange String k Distance Apart
// https://leetcode.com/problems/rearrange-string-k-distance-apart/

#include <stdlib.h>
#include <string.h>

typedef struct {
    char ch;
    int count;
    int readyAt;
} QueueItem;

typedef struct {
    char ch;
    int count;
} HeapItem;

static int compareHeapItems(const void* leftPtr, const void* rightPtr) {
    const HeapItem* left = (const HeapItem*)leftPtr;
    const HeapItem* right = (const HeapItem*)rightPtr;
    if (left->count != right->count) {
        return right->count - left->count;
    }
    return (int)left->ch - (int)right->ch;
}

static void heapPush(HeapItem* heap, int* heapSize, char ch, int count) {
    heap[*heapSize].ch = ch;
    heap[*heapSize].count = count;
    *heapSize += 1;
    qsort(heap, (size_t)*heapSize, sizeof(HeapItem), compareHeapItems);
}

static HeapItem heapPop(HeapItem* heap, int* heapSize) {
    HeapItem top = heap[0];
    heap[0] = heap[*heapSize - 1];
    *heapSize -= 1;
    if (*heapSize > 0) {
        qsort(heap, (size_t)*heapSize, sizeof(HeapItem), compareHeapItems);
    }
    return top;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char* rearrangeString(char* s, int k) {
    int counts[256] = {0};
    int length = (int)strlen(s);
    for (int index = 0; index < length; index++) {
        counts[(unsigned char)s[index]] += 1;
    }

    int maxFreq = 0;
    for (int ch = 0; ch < 256; ch++) {
        if (counts[ch] > maxFreq) {
            maxFreq = counts[ch];
        }
    }

    int maxFreqChars = 0;
    for (int ch = 0; ch < 256; ch++) {
        if (counts[ch] == maxFreq) {
            maxFreqChars += 1;
        }
    }

    if ((length - maxFreqChars) < (maxFreq - 1) * (k - 1)) {
        char* empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }

    HeapItem* heap = (HeapItem*)malloc((size_t)length * sizeof(HeapItem));
    int heapSize = 0;
    for (int ch = 0; ch < 256; ch++) {
        if (counts[ch] > 0) {
            heapPush(heap, &heapSize, (char)ch, counts[ch]);
        }
    }

    QueueItem* queue = (QueueItem*)malloc((size_t)length * sizeof(QueueItem));
    int queueSize = 0;
    char* result = (char*)malloc((size_t)(length + 1) * sizeof(char));
    int resultSize = 0;
    int index = 0;

    while (heapSize > 0 || queueSize > 0) {
        while (queueSize > 0 && queue[0].readyAt <= index) {
            QueueItem item = queue[0];
            queueSize -= 1;
            for (int queueIndex = 0; queueIndex < queueSize; queueIndex++) {
                queue[queueIndex] = queue[queueIndex + 1];
            }
            heapPush(heap, &heapSize, item.ch, item.count);
        }

        if (heapSize == 0) {
            free(heap);
            free(queue);
            free(result);
            char* empty = (char*)malloc(1);
            empty[0] = '\0';
            return empty;
        }

        HeapItem top = heapPop(heap, &heapSize);
        result[resultSize++] = top.ch;
        if (top.count - 1 > 0) {
            queue[queueSize].ch = top.ch;
            queue[queueSize].count = top.count - 1;
            queue[queueSize].readyAt = index + k;
            queueSize += 1;
        }
        index += 1;
    }

    result[resultSize] = '\0';
    free(heap);
    free(queue);
    return result;
}
