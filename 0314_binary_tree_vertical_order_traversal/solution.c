// LeetCode 0314 - Binary Tree Vertical Order Traversal
// https://leetcode.com/problems/binary-tree-vertical-order-traversal/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

typedef struct {
    struct TreeNode* node;
    int column;
} QueueEntry;

typedef struct {
    int column;
    int* values;
    int size;
    int capacity;
} ColumnBucket;

static void appendValue(ColumnBucket* bucket, int value) {
    if (bucket->size == bucket->capacity) {
        bucket->capacity = bucket->capacity ? bucket->capacity * 2 : 4;
        bucket->values = (int*)realloc(bucket->values, (size_t)bucket->capacity * sizeof(int));
    }
    bucket->values[bucket->size++] = value;
}

static ColumnBucket* getOrCreate(ColumnBucket** buckets, int* bucketCount, int* bucketCapacity, int column) {
    for (int index = 0; index < *bucketCount; index++) {
        if ((*buckets)[index].column == column) {
            return &(*buckets)[index];
        }
    }
    if (*bucketCount == *bucketCapacity) {
        *bucketCapacity = *bucketCapacity ? *bucketCapacity * 2 : 8;
        *buckets = (ColumnBucket*)realloc(*buckets, (size_t)(*bucketCapacity) * sizeof(ColumnBucket));
    }
    ColumnBucket* bucket = &(*buckets)[*bucketCount];
    bucket->column = column;
    bucket->values = NULL;
    bucket->size = 0;
    bucket->capacity = 0;
    (*bucketCount)++;
    return bucket;
}

static int compareBuckets(const void* left, const void* right) {
    const ColumnBucket* leftBucket = (const ColumnBucket*)left;
    const ColumnBucket* rightBucket = (const ColumnBucket*)right;
    return leftBucket->column - rightBucket->column;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced, assume caller calls free().
 */
int** verticalOrder(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {
    if (root == NULL) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    QueueEntry* queue = (QueueEntry*)malloc(4096 * sizeof(QueueEntry));
    int front = 0;
    int rear = 0;
    queue[rear++] = (QueueEntry){root, 0};

    ColumnBucket* buckets = NULL;
    int bucketCount = 0;
    int bucketCapacity = 0;

    while (front < rear) {
        QueueEntry entry = queue[front++];
        ColumnBucket* bucket = getOrCreate(&buckets, &bucketCount, &bucketCapacity, entry.column);
        appendValue(bucket, entry.node->val);
        if (entry.node->left != NULL) {
            queue[rear++] = (QueueEntry){entry.node->left, entry.column - 1};
        }
        if (entry.node->right != NULL) {
            queue[rear++] = (QueueEntry){entry.node->right, entry.column + 1};
        }
    }

    qsort(buckets, (size_t)bucketCount, sizeof(ColumnBucket), compareBuckets);

    int** result = (int**)malloc((size_t)bucketCount * sizeof(int*));
    int* colSizes = (int*)malloc((size_t)bucketCount * sizeof(int));
    for (int index = 0; index < bucketCount; index++) {
        result[index] = buckets[index].values;
        colSizes[index] = buckets[index].size;
    }

    free(buckets);
    free(queue);
    *returnSize = bucketCount;
    *returnColumnSizes = colSizes;
    return result;
}
