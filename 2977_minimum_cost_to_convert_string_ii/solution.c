// LeetCode 2977 - Minimum Cost to Convert String II
// https://leetcode.com/problems/minimum-cost-to-convert-string-ii/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct {
    char* key;
    int id;
    int used;
} SM2977;

static unsigned shash2977(const char* s, int len) {
    unsigned h = 5381;
    for (int i = 0; i < len; i++) h = ((h << 5) + h) + (unsigned char)s[i];
    return h;
}

static int smGetOrAdd2977(SM2977* t, int cap, const char* s, int len, int* nextId) {
    unsigned i = shash2977(s, len) & (unsigned)(cap - 1);
    while (t[i].used) {
        if ((int)strlen(t[i].key) == len && strncmp(t[i].key, s, (size_t)len) == 0) return t[i].id;
        i = (i + 1) & (unsigned)(cap - 1);
    }
    t[i].used = 1;
    t[i].key = (char*)malloc((size_t)len + 1);
    memcpy(t[i].key, s, (size_t)len);
    t[i].key[len] = '\0';
    t[i].id = (*nextId)++;
    return t[i].id;
}

static int smGet2977(SM2977* t, int cap, const char* s, int len) {
    unsigned i = shash2977(s, len) & (unsigned)(cap - 1);
    while (t[i].used) {
        if ((int)strlen(t[i].key) == len && strncmp(t[i].key, s, (size_t)len) == 0) return t[i].id;
        i = (i + 1) & (unsigned)(cap - 1);
    }
    return -1;
}

long long minimumCost(char* source, char* target, char** original, int originalSize, char** changed, int changedSize, int* cost, int costSize) {
    (void)changedSize;
    (void)costSize;
    const long long INF = 1LL << 60;
    int cap = 1;
    while (cap < (originalSize + changedSize) * 4 + 16) cap <<= 1;
    SM2977* ids = (SM2977*)calloc((size_t)cap, sizeof(SM2977));
    int nextId = 0;
    for (int i = 0; i < originalSize; i++) {
        smGetOrAdd2977(ids, cap, original[i], (int)strlen(original[i]), &nextId);
        smGetOrAdd2977(ids, cap, changed[i], (int)strlen(changed[i]), &nextId);
    }
    int m = nextId;
    long long** dist = (long long**)malloc((size_t)m * sizeof(long long*));
    for (int i = 0; i < m; i++) {
        dist[i] = (long long*)malloc((size_t)m * sizeof(long long));
        for (int j = 0; j < m; j++) dist[i][j] = (i == j) ? 0 : INF;
    }
    for (int i = 0; i < originalSize; i++) {
        int u = smGet2977(ids, cap, original[i], (int)strlen(original[i]));
        int v = smGet2977(ids, cap, changed[i], (int)strlen(changed[i]));
        long long w = cost[i];
        if (w < dist[u][v]) dist[u][v] = w;
    }
    for (int k = 0; k < m; k++) {
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                if (dist[i][k] + dist[k][j] < dist[i][j]) dist[i][j] = dist[i][k] + dist[k][j];
            }
        }
    }
    int n = (int)strlen(source);
    long long* dp = (long long*)malloc((size_t)(n + 1) * sizeof(long long));
    for (int i = 0; i <= n; i++) dp[i] = INF;
    dp[0] = 0;
    bool lensMark[51] = {0};
    int lens[64];
    int ln = 0;
    for (int i = 0; i < cap; i++) {
        if (!ids[i].used) continue;
        int L = (int)strlen(ids[i].key);
        if (L <= 50 && !lensMark[L]) {
            lensMark[L] = true;
            lens[ln++] = L;
        }
    }
    for (int i = 0; i < n; i++) {
        if (dp[i] >= INF / 2) continue;
        if (source[i] == target[i] && dp[i] < dp[i + 1]) dp[i + 1] = dp[i];
        for (int li = 0; li < ln; li++) {
            int L = lens[li];
            if (i + L > n) continue;
            int u = smGet2977(ids, cap, source + i, L);
            int v = smGet2977(ids, cap, target + i, L);
            if (u < 0 || v < 0) continue;
            if (dist[u][v] < INF / 2) {
                long long cand = dp[i] + dist[u][v];
                if (cand < dp[i + L]) dp[i + L] = cand;
            }
        }
    }
    long long ans = (dp[n] >= INF / 2) ? -1 : dp[n];
    free(dp);
    for (int i = 0; i < m; i++) free(dist[i]);
    free(dist);
    for (int i = 0; i < cap; i++) if (ids[i].used) free(ids[i].key);
    free(ids);
    return ans;
}
