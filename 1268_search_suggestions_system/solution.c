// LeetCode 1268 - Search Suggestions System
// https://leetcode.com/problems/search-suggestions-system/

#include <stdlib.h>
#include <string.h>

static int cmp_str(const void* a, const void* b) {
    return strcmp(*(const char* const*)a, *(const char* const*)b);
}

char*** suggestedProducts(char** products, int productsSize, char* searchWord, int* returnSize, int** returnColumnSizes) {
    qsort(products, (size_t)productsSize, sizeof(char*), cmp_str);
    int n = (int)strlen(searchWord);
    char*** ans = (char***)malloc((size_t)n * sizeof(char**));
    *returnColumnSizes = (int*)malloc((size_t)n * sizeof(int));
    *returnSize = n;
    for (int i = 0; i < n; i++) {
        int lo = 0, hi = productsSize - 1, start = productsSize;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (strncmp(products[mid], searchWord, (size_t)i + 1) >= 0) {
                start = mid;
                hi = mid - 1;
            } else lo = mid + 1;
        }
        int count = 0;
        char** row = (char**)malloc(3 * sizeof(char*));
        for (int j = start; j < productsSize && count < 3; j++) {
            if (strncmp(products[j], searchWord, (size_t)i + 1) == 0) row[count++] = products[j];
            else break;
        }
        ans[i] = row;
        (*returnColumnSizes)[i] = count;
    }
    return ans;
}
