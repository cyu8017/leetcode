// LeetCode 0632 - Smallest Range Covering Elements from K Lists
// https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

#include <limits.h>
#include <stdlib.h>

typedef struct {
    int value;
    int listIndex;
    int index;
} Node;

static void heapSwap(Node* a, Node* b) {
    Node t = *a;
    *a = *b;
    *b = t;
}

static void heapPush(Node* heap, int* size, Node node) {
    int i = (*size)++;
    heap[i] = node;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (heap[p].value <= heap[i].value) {
            break;
        }
        heapSwap(&heap[p], &heap[i]);
        i = p;
    }
}

static Node heapPop(Node* heap, int* size) {
    Node top = heap[0];
    heap[0] = heap[--(*size)];
    int i = 0;
    while (1) {
        int smallest = i;
        int l = 2 * i + 1, r = 2 * i + 2;
        if (l < *size && heap[l].value < heap[smallest].value) {
            smallest = l;
        }
        if (r < *size && heap[r].value < heap[smallest].value) {
            smallest = r;
        }
        if (smallest == i) {
            break;
        }
        heapSwap(&heap[i], &heap[smallest]);
        i = smallest;
    }
    return top;
}

int* smallestRange(int** nums, int numsSize, int* numsColSize, int* returnSize) {
    Node* heap = (Node*)malloc((size_t)numsSize * sizeof(Node));
    int heapSize = 0;
    int currentMax = INT_MIN;
    for (int i = 0; i < numsSize; i++) {
        Node node = {nums[i][0], i, 0};
        heapPush(heap, &heapSize, node);
        if (nums[i][0] > currentMax) {
            currentMax = nums[i][0];
        }
    }
    int bestLeft = heap[0].value;
    int bestRight = currentMax;
    while (1) {
        Node cur = heapPop(heap, &heapSize);
        if (currentMax - cur.value < bestRight - bestLeft) {
            bestLeft = cur.value;
            bestRight = currentMax;
        }
        if (cur.index + 1 == numsColSize[cur.listIndex]) {
            break;
        }
        int nxt = nums[cur.listIndex][cur.index + 1];
        Node node = {nxt, cur.listIndex, cur.index + 1};
        heapPush(heap, &heapSize, node);
        if (nxt > currentMax) {
            currentMax = nxt;
        }
    }
    free(heap);
    int* result = (int*)malloc(2 * sizeof(int));
    result[0] = bestLeft;
    result[1] = bestRight;
    *returnSize = 2;
    return result;
}
