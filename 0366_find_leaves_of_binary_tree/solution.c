// LeetCode 0366 - Find Leaves of Binary Tree
// https://leetcode.com/problems/find-leaves-of-binary-tree/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

typedef struct {
    int** layers;
    int* layerSizes;
    int layerCount;
    int layerCapacity;
} LayerCollector;

static void ensureLayer(LayerCollector* collector, int height) {
    while (collector->layerCount <= height) {
        if (collector->layerCount >= collector->layerCapacity) {
            collector->layerCapacity = collector->layerCapacity == 0 ? 4 : collector->layerCapacity * 2;
            collector->layers = (int**)realloc(
                collector->layers, (size_t)collector->layerCapacity * sizeof(int*));
            collector->layerSizes = (int*)realloc(
                collector->layerSizes, (size_t)collector->layerCapacity * sizeof(int));
        }
        collector->layers[collector->layerCount] = NULL;
        collector->layerSizes[collector->layerCount] = 0;
        collector->layerCount += 1;
    }
}

static void appendValue(LayerCollector* collector, int height, int value) {
    ensureLayer(collector, height);
    collector->layerSizes[height] += 1;
    collector->layers[height] = (int*)realloc(
        collector->layers[height], (size_t)collector->layerSizes[height] * sizeof(int));
    collector->layers[height][collector->layerSizes[height] - 1] = value;
}

static int dfs(struct TreeNode* node, LayerCollector* collector) {
    if (node == NULL) {
        return -1;
    }

    int leftHeight = dfs(node->left, collector);
    int rightHeight = dfs(node->right, collector);
    int height = (leftHeight > rightHeight ? leftHeight : rightHeight) + 1;
    appendValue(collector, height, node->val);
    return height;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced, assume caller calls free().
 */
int** findLeaves(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {
    LayerCollector collector = {NULL, NULL, 0, 0};
    dfs(root, &collector);

    *returnSize = collector.layerCount;
    if (collector.layerCount == 0) {
        *returnColumnSizes = NULL;
        return NULL;
    }

    int** result = (int**)malloc((size_t)collector.layerCount * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)collector.layerCount * sizeof(int));

    for (int index = 0; index < collector.layerCount; index++) {
        (*returnColumnSizes)[index] = collector.layerSizes[index];
        result[index] = collector.layers[index];
    }

    free(collector.layers);
    free(collector.layerSizes);
    return result;
}
