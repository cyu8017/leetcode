// LeetCode 1415 - The k-th Lexicographical String of All Happy Strings of Length n
// https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

#include <stdlib.h>
#include <string.h>

static char** list;
static int listSize, listCap, N;

static void build(char* path, int len) {
    if (len == N) {
        if (listSize == listCap) {
            listCap *= 2;
            list = (char**)realloc(list, listCap * sizeof(char*));
        }
        list[listSize] = (char*)malloc(N + 1);
        memcpy(list[listSize], path, N);
        list[listSize][N] = '\0';
        listSize++;
        return;
    }
    for (char c = 'a'; c <= 'c'; c++) {
        if (len == 0 || path[len - 1] != c) {
            path[len] = c;
            build(path, len + 1);
        }
    }
}

char* getHappyString(int n, int k) {
    N = n; listCap = 64; listSize = 0;
    list = (char**)malloc(listCap * sizeof(char*));
    char* path = (char*)malloc(n + 1);
    build(path, 0);
    free(path);
    char* ans;
    if (k <= listSize) {
        ans = list[k - 1];
        for (int i = 0; i < listSize; i++) if (i != k - 1) free(list[i]);
    } else {
        ans = (char*)malloc(1); ans[0] = '\0';
        for (int i = 0; i < listSize; i++) free(list[i]);
    }
    free(list);
    return ans;
}
