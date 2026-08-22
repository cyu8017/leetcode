// LeetCode 0721 - Accounts Merge
// https://leetcode.com/problems/accounts-merge/

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct {
    char* email;
    char* name;
    int parent;
} EmailNode;

static int findParent(int* parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static int cmpStrPtr(const void* a, const void* b) {
    return strcmp(*(char* const*)a, *(char* const*)b);
}

static int emailIndex(EmailNode* nodes, int n, const char* email) {
    for (int i = 0; i < n; i++) {
        if (strcmp(nodes[i].email, email) == 0) {
            return i;
        }
    }
    return -1;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char*** accountsMerge(char*** accounts, int accountsSize, int* accountsColSize, int* returnSize, int** returnColumnSizes) {
    int cap = 0;
    for (int i = 0; i < accountsSize; i++) {
        cap += accountsColSize[i] - 1;
    }
    EmailNode* nodes = (EmailNode*)malloc((size_t)cap * sizeof(EmailNode));
    int* parent = (int*)malloc((size_t)cap * sizeof(int));
    int n = 0;

    for (int i = 0; i < accountsSize; i++) {
        char* name = accounts[i][0];
        int first = -1;
        for (int j = 1; j < accountsColSize[i]; j++) {
            char* email = accounts[i][j];
            int idx = emailIndex(nodes, n, email);
            if (idx < 0) {
                idx = n;
                nodes[n].email = email;
                nodes[n].name = name;
                parent[n] = n;
                n++;
            }
            if (first < 0) {
                first = idx;
            } else {
                int a = findParent(parent, first);
                int b = findParent(parent, idx);
                parent[a] = b;
            }
        }
    }

    char*** groups = (char***)calloc((size_t)n, sizeof(char**));
    int* groupSizes = (int*)calloc((size_t)n, sizeof(int));
    int* groupCaps = (int*)calloc((size_t)n, sizeof(int));
    char** groupNames = (char**)calloc((size_t)n, sizeof(char*));

    for (int i = 0; i < n; i++) {
        int root = findParent(parent, i);
        if (groupSizes[root] == groupCaps[root]) {
            groupCaps[root] = groupCaps[root] ? groupCaps[root] * 2 : 4;
            groups[root] = (char**)realloc(groups[root], (size_t)groupCaps[root] * sizeof(char*));
        }
        groups[root][groupSizes[root]++] = nodes[i].email;
        groupNames[root] = nodes[i].name;
    }

    char*** result = (char***)malloc((size_t)n * sizeof(char**));
    *returnColumnSizes = (int*)malloc((size_t)n * sizeof(int));
    int rsize = 0;
    for (int i = 0; i < n; i++) {
        if (groupSizes[i] == 0) {
            continue;
        }
        qsort(groups[i], (size_t)groupSizes[i], sizeof(char*), cmpStrPtr);
        int cols = groupSizes[i] + 1;
        result[rsize] = (char**)malloc((size_t)cols * sizeof(char*));
        result[rsize][0] = (char*)malloc(strlen(groupNames[i]) + 1);
        strcpy(result[rsize][0], groupNames[i]);
        for (int j = 0; j < groupSizes[i]; j++) {
            result[rsize][j + 1] = (char*)malloc(strlen(groups[i][j]) + 1);
            strcpy(result[rsize][j + 1], groups[i][j]);
        }
        (*returnColumnSizes)[rsize] = cols;
        rsize++;
        free(groups[i]);
    }

    free(groups);
    free(groupSizes);
    free(groupCaps);
    free(groupNames);
    free(nodes);
    free(parent);
    *returnSize = rsize;
    return result;
}
