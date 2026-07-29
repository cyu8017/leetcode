// LeetCode 1418 - Display Table of Food Orders in a Restaurant
// https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

static int cmp_str(const void* a, const void* b) { return strcmp(*(char**)a, *(char**)b); }
static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

char*** displayTable(char*** orders, int ordersSize, int* ordersColSize, int* returnSize, int** returnColumnSizes) {
    (void)ordersColSize;
    char** foods = (char**)malloc(ordersSize * sizeof(char*));
    int fn = 0;
    int* tables = (int*)malloc(ordersSize * sizeof(int));
    int tn = 0;
    for (int i = 0; i < ordersSize; i++) {
        char* food = orders[i][2];
        int found = 0;
        for (int j = 0; j < fn; j++) if (strcmp(foods[j], food) == 0) { found = 1; break; }
        if (!found) foods[fn++] = food;
        int table = atoi(orders[i][1]);
        found = 0;
        for (int j = 0; j < tn; j++) if (tables[j] == table) { found = 1; break; }
        if (!found) tables[tn++] = table;
    }
    qsort(foods, fn, sizeof(char*), cmp_str);
    qsort(tables, tn, sizeof(int), cmp_int);
    int* counts = (int*)calloc(tn * fn, sizeof(int));
    for (int i = 0; i < ordersSize; i++) {
        int table = atoi(orders[i][1]);
        char* food = orders[i][2];
        int ti = 0, fi = 0;
        while (tables[ti] != table) ti++;
        while (strcmp(foods[fi], food)) fi++;
        counts[ti * fn + fi]++;
    }
    int rows = tn + 1, cols = fn + 1;
    char*** ans = (char***)malloc(rows * sizeof(char**));
    *returnColumnSizes = (int*)malloc(rows * sizeof(int));
    for (int r = 0; r < rows; r++) {
        ans[r] = (char**)malloc(cols * sizeof(char*));
        (*returnColumnSizes)[r] = cols;
    }
    ans[0][0] = (char*)malloc(6); strcpy(ans[0][0], "Table");
    for (int j = 0; j < fn; j++) {
        ans[0][j + 1] = (char*)malloc(strlen(foods[j]) + 1);
        strcpy(ans[0][j + 1], foods[j]);
    }
    for (int i = 0; i < tn; i++) {
        ans[i + 1][0] = (char*)malloc(16);
        sprintf(ans[i + 1][0], "%d", tables[i]);
        for (int j = 0; j < fn; j++) {
            ans[i + 1][j + 1] = (char*)malloc(16);
            sprintf(ans[i + 1][j + 1], "%d", counts[i * fn + j]);
        }
    }
    free(foods); free(tables); free(counts);
    *returnSize = rows;
    return ans;
}
