// LeetCode 0753 - Cracking the Safe
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

static char* g_seen;
static char* g_path;
static int g_pathLen;
static int g_n, g_k;

static int edgeIndex(const char* edge) {
    int idx = 0;
    for (const char* p = edge; *p; p++) idx = idx * g_k + (*p - '0');
    return idx;
}

static void dfsCrack(const char* node) {
    for (int d = 0; d < g_k; d++) {
        char edge[16];
        snprintf(edge, sizeof(edge), "%s%c", node, '0' + d);
        int idx = edgeIndex(edge);
        if (!g_seen[idx]) {
            g_seen[idx] = 1;
            dfsCrack(edge + 1);
            g_path[g_pathLen++] = (char)('0' + d);
        }
    }
}

char* crackSafe(int n, int k) {
    g_n = n; g_k = k;
    int edgeSpace = 1;
    for (int i = 0; i < n; i++) edgeSpace *= k;
    g_seen = (char*)calloc((size_t)edgeSpace, 1);
    g_path = (char*)malloc((size_t)edgeSpace + n + 2);
    g_pathLen = 0;
    char start[16];
    for (int i = 0; i < n - 1; i++) start[i] = '0';
    start[n > 0 ? n - 1 : 0] = '\0';
    if (n == 1) start[0] = '\0';
    dfsCrack(start);
    for (int i = 0; i < n - 1; i++) g_path[g_pathLen++] = '0';
    g_path[g_pathLen] = '\0';
    free(g_seen);
    return g_path;
}
