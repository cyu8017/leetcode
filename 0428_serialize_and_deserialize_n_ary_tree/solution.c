// LeetCode 0428 - Serialize and Deserialize N-ary Tree
// https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

#define _POSIX_C_SOURCE 200809L

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Node {
    int val;
    int numChildren;
    struct Node** children;
};

typedef struct {
    char* data;
    int size;
    int capacity;
} StrBuf;

static void bufAppend(StrBuf* buf, const char* text) {
    int len = (int)strlen(text);
    if (buf->size + len + 1 > buf->capacity) {
        buf->capacity = (buf->capacity == 0 ? 64 : buf->capacity * 2) + len;
        buf->data = (char*)realloc(buf->data, (size_t)buf->capacity);
    }
    memcpy(buf->data + buf->size, text, (size_t)len);
    buf->size += len;
    buf->data[buf->size] = '\0';
}

char* serialize(struct Node* root) {
    if (root == NULL) {
        char* empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }

    StrBuf buf = {0};
    struct Node** queue = (struct Node**)malloc(10000 * sizeof(struct Node*));
    int head = 0;
    int tail = 0;
    queue[tail++] = root;

    while (head < tail) {
        struct Node* node = queue[head++];
        char text[32];
        if (buf.size > 0) {
            bufAppend(&buf, ",");
        }
        sprintf(text, "%d", node->val);
        bufAppend(&buf, text);
        bufAppend(&buf, ",");
        sprintf(text, "%d", node->numChildren);
        bufAppend(&buf, text);
        for (int i = 0; i < node->numChildren; i++) {
            bufAppend(&buf, ",");
            sprintf(text, "%d", node->children[i]->val);
            bufAppend(&buf, text);
            queue[tail++] = node->children[i];
        }
    }
    free(queue);
    return buf.data;
}

struct Node* deserialize(char* data) {
    if (data == NULL || data[0] == '\0') {
        return NULL;
    }

    char* copy = strdup(data);
    int count = 1;
    for (int i = 0; copy[i]; i++) {
        if (copy[i] == ',') {
            count++;
        }
    }
    int* values = (int*)malloc((size_t)count * sizeof(int));
    int idx = 0;
    char* save = NULL;
    char* token = strtok_r(copy, ",", &save);
    while (token) {
        values[idx++] = atoi(token);
        token = strtok_r(NULL, ",", &save);
    }

    int index = 0;
    struct Node* root = (struct Node*)malloc(sizeof(struct Node));
    root->val = values[index++];
    root->numChildren = values[index++];
    root->children = root->numChildren ? (struct Node**)malloc((size_t)root->numChildren * sizeof(struct Node*)) : NULL;
    for (int i = 0; i < root->numChildren; i++) {
        root->children[i] = (struct Node*)malloc(sizeof(struct Node));
        root->children[i]->val = values[index++];
        root->children[i]->numChildren = 0;
        root->children[i]->children = NULL;
    }

    struct Node** queue = (struct Node**)malloc(10000 * sizeof(struct Node*));
    int head = 0;
    int tail = 0;
    for (int i = 0; i < root->numChildren; i++) {
        queue[tail++] = root->children[i];
    }

    while (head < tail) {
        struct Node* node = queue[head++];
        int value = values[index++];
        int childCount = values[index++];
        (void)value;
        node->numChildren = childCount;
        node->children = childCount ? (struct Node**)malloc((size_t)childCount * sizeof(struct Node*)) : NULL;
        for (int i = 0; i < childCount; i++) {
            node->children[i] = (struct Node*)malloc(sizeof(struct Node));
            node->children[i]->val = values[index++];
            node->children[i]->numChildren = 0;
            node->children[i]->children = NULL;
            queue[tail++] = node->children[i];
        }
    }

    free(queue);
    free(values);
    free(copy);
    return root;
}
