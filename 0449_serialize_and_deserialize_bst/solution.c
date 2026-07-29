// LeetCode 0449 - Serialize and Deserialize BST
// https://leetcode.com/problems/serialize-and-deserialize-bst/

#define _POSIX_C_SOURCE 200809L

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
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

static void preorder(struct TreeNode* node, StrBuf* buf) {
    if (buf->size > 0) {
        bufAppend(buf, ",");
    }
    if (node == NULL) {
        bufAppend(buf, "#");
        return;
    }
    char text[32];
    sprintf(text, "%d", node->val);
    bufAppend(buf, text);
    preorder(node->left, buf);
    preorder(node->right, buf);
}

char* serialize(struct TreeNode* root) {
    StrBuf buf = {0};
    preorder(root, &buf);
    if (buf.data == NULL) {
        buf.data = strdup("");
    }
    return buf.data;
}

static struct TreeNode* build(char*** tokens) {
    char* token = **tokens;
    (*tokens)++;
    if (strcmp(token, "#") == 0) {
        return NULL;
    }
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = atoi(token);
    node->left = build(tokens);
    node->right = build(tokens);
    return node;
}

struct TreeNode* deserialize(char* data) {
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
    char** tokens = (char**)malloc((size_t)count * sizeof(char*));
    int idx = 0;
    char* save = NULL;
    char* token = strtok_r(copy, ",", &save);
    while (token) {
        tokens[idx++] = token;
        token = strtok_r(NULL, ",", &save);
    }
    char** cursor = tokens;
    struct TreeNode* root = build(&cursor);
    free(tokens);
    free(copy);
    return root;
}
