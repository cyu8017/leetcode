// LeetCode 0354 - Russian Doll Envelopes
// https://leetcode.com/problems/russian-doll-envelopes/

#include <stdlib.h>

typedef struct {
    int width;
    int height;
} Envelope;

static int compareEnvelopes(const void* leftPtr, const void* rightPtr) {
    const Envelope* left = (const Envelope*)leftPtr;
    const Envelope* right = (const Envelope*)rightPtr;
    if (left->width != right->width) {
        return left->width - right->width;
    }
    return right->height - left->height;
}

static int lowerBound(const int* tails, int tailsSize, int value) {
    int left = 0;
    int right = tailsSize;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (tails[mid] < value) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
}

int maxEnvelopes(int** envelopes, int envelopesSize, int* envelopesColSize) {
    Envelope* items = (Envelope*)malloc((size_t)envelopesSize * sizeof(Envelope));
    for (int index = 0; index < envelopesSize; index++) {
        items[index].width = envelopes[index][0];
        items[index].height = envelopes[index][1];
    }

    qsort(items, (size_t)envelopesSize, sizeof(Envelope), compareEnvelopes);

    int* tails = (int*)malloc((size_t)envelopesSize * sizeof(int));
    int tailsSize = 0;

    for (int index = 0; index < envelopesSize; index++) {
        int height = items[index].height;
        int position = lowerBound(tails, tailsSize, height);
        if (position == tailsSize) {
            tails[tailsSize++] = height;
        } else {
            tails[position] = height;
        }
    }

    free(items);
    free(tails);
    return tailsSize;
}
