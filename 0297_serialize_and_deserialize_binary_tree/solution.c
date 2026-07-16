// LeetCode 0297 - Serialize and Deserialize Binary Tree
// https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

typedef struct {
    struct TreeNode** data;
    int front;
    int back;
    int capacity;
} TreeQueue;

static void treeQueueInit(TreeQueue* queue) {
    queue->capacity = 16;
    queue->data = (struct TreeNode**)malloc((size_t)queue->capacity * sizeof(struct TreeNode*));
    queue->front = 0;
    queue->back = 0;
}

static void treeQueuePush(TreeQueue* queue, struct TreeNode* node) {
    if (queue->back >= queue->capacity) {
        queue->capacity *= 2;
        queue->data = (struct TreeNode**)realloc(queue->data, (size_t)queue->capacity * sizeof(struct TreeNode*));
    }
    queue->data[queue->back++] = node;
}

static struct TreeNode* treeQueuePop(TreeQueue* queue) {
    return queue->data[queue->front++];
}

static int treeQueueEmpty(TreeQueue* queue) {
    return queue->front >= queue->back;
}

static void treeQueueFree(TreeQueue* queue) {
    free(queue->data);
}

char* serialize(struct TreeNode* root) {
    if (root == NULL) {
        char* empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }

    char** values = NULL;
    int valueCount = 0;
    int valueCapacity = 0;

    TreeQueue queue;
    treeQueueInit(&queue);
    treeQueuePush(&queue, root);

    while (!treeQueueEmpty(&queue)) {
        struct TreeNode* node = treeQueuePop(&queue);
        if (valueCount == valueCapacity) {
            valueCapacity = valueCapacity == 0 ? 16 : valueCapacity * 2;
            values = (char**)realloc(values, (size_t)valueCapacity * sizeof(char*));
        }
        if (node == NULL) {
            values[valueCount++] = strdup("");
        } else {
            char buffer[32];
            snprintf(buffer, sizeof(buffer), "%d", node->val);
            values[valueCount++] = strdup(buffer);
            treeQueuePush(&queue, node->left);
            treeQueuePush(&queue, node->right);
        }
    }

    while (valueCount > 0 && strcmp(values[valueCount - 1], "") == 0) {
        free(values[--valueCount]);
    }

    size_t total = 1;
    for (int index = 0; index < valueCount; index++) {
        total += strlen(values[index]) + 1;
    }

    char* encoded = (char*)malloc(total);
    encoded[0] = '\0';
    for (int index = 0; index < valueCount; index++) {
        if (index > 0) {
            strcat(encoded, ",");
        }
        strcat(encoded, values[index]);
        free(values[index]);
    }
    free(values);
    treeQueueFree(&queue);
    return encoded;
}

struct TreeNode* deserialize(char* data) {
    if (data == NULL || data[0] == '\0') {
        return NULL;
    }

    int tokenCount = 1;
    for (char* cursor = data; *cursor; cursor++) {
        if (*cursor == ',') {
            tokenCount++;
        }
    }

    char** tokens = (char**)malloc((size_t)tokenCount * sizeof(char*));
    int index = 0;
    char* copy = strdup(data);
    char* token = strtok(copy, ",");
    while (token != NULL) {
        tokens[index++] = token;
        token = strtok(NULL, ",");
    }

    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val = atoi(tokens[0]);
    root->left = NULL;
    root->right = NULL;

    TreeQueue queue;
    treeQueueInit(&queue);
    treeQueuePush(&queue, root);
    int tokenIndex = 1;

    while (!treeQueueEmpty(&queue) && tokenIndex < index) {
        struct TreeNode* node = treeQueuePop(&queue);

        if (tokenIndex < index && tokens[tokenIndex][0] != '\0') {
            node->left = (struct TreeNode*)malloc(sizeof(struct TreeNode));
            node->left->val = atoi(tokens[tokenIndex]);
            node->left->left = NULL;
            node->left->right = NULL;
            treeQueuePush(&queue, node->left);
        }
        tokenIndex++;

        if (tokenIndex < index && tokens[tokenIndex][0] != '\0') {
            node->right = (struct TreeNode*)malloc(sizeof(struct TreeNode));
            node->right->val = atoi(tokens[tokenIndex]);
            node->right->left = NULL;
            node->right->right = NULL;
            treeQueuePush(&queue, node->right);
        }
        tokenIndex++;
    }

    free(copy);
    free(tokens);
    treeQueueFree(&queue);
    return root;
}
