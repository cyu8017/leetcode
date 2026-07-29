// LeetCode 0756 - Pyramid Transition Matrix
// https://leetcode.com/problems/pyramid-transition-matrix/

#include <stdbool.h>
#include <string.h>

static char g_choices[26][26][8];
static int g_choiceCount[26][26];
static char g_memo[1 << 18];
static char g_memoHas[1 << 18];

static unsigned hashRow(const char* row) {
    unsigned h = 2166136261u;
    for (const char* p = row; *p; p++) {
        h ^= (unsigned char)(*p);
        h *= 16777619u;
    }
    return h & ((1u << 18) - 1);
}

static bool dfsRow(const char* row);

static bool buildNext(char opts[][8], int* optLens, int optCount, int index, char* path) {
    if (index == optCount) {
        path[optCount] = '\0';
        return dfsRow(path);
    }
    for (int c = 0; c < optLens[index]; c++) {
        path[index] = opts[index][c];
        if (buildNext(opts, optLens, optCount, index + 1, path)) {
            return true;
        }
    }
    return false;
}

static bool dfsRow(const char* row) {
    int len = (int)strlen(row);
    if (len == 1) {
        return true;
    }
    unsigned h = hashRow(row);
    if (g_memoHas[h]) {
        return g_memo[h] != 0;
    }
    char opts[16][8];
    int optLens[16];
    int optCount = 0;
    for (int i = 0; i < len - 1; i++) {
        int a = row[i] - 'A';
        int b = row[i + 1] - 'A';
        if (g_choiceCount[a][b] == 0) {
            g_memoHas[h] = 1;
            g_memo[h] = 0;
            return false;
        }
        for (int c = 0; c < g_choiceCount[a][b]; c++) {
            opts[optCount][c] = g_choices[a][b][c];
        }
        optLens[optCount] = g_choiceCount[a][b];
        optCount++;
    }
    char path[16];
    bool ok = buildNext(opts, optLens, optCount, 0, path);
    g_memoHas[h] = 1;
    g_memo[h] = ok ? 1 : 0;
    return ok;
}

bool pyramidTransition(char* bottom, char** allowed, int allowedSize) {
    memset(g_choiceCount, 0, sizeof(g_choiceCount));
    memset(g_memoHas, 0, sizeof(g_memoHas));
    for (int i = 0; i < allowedSize; i++) {
        int a = allowed[i][0] - 'A';
        int b = allowed[i][1] - 'A';
        g_choices[a][b][g_choiceCount[a][b]++] = allowed[i][2];
    }
    return dfsRow(bottom);
}
