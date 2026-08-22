// LeetCode 1583 - Count Unhappy Friends
// https://leetcode.com/problems/count-unhappy-friends/

#include <stdlib.h>

int unhappyFriends(int n, int** preferences, int preferencesSize, int* preferencesColSize, int** pairs, int pairsSize, int* pairsColSize) {
    (void)preferencesSize; (void)preferencesColSize; (void)pairsColSize;
    int** rank = (int**)malloc((size_t)n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        rank[i] = (int*)malloc((size_t)n * sizeof(int));
        for (int j = 0; j < n - 1; j++) rank[i][preferences[i][j]] = j;
    }
    int* partner = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < pairsSize; i++) {
        int a = pairs[i][0], b = pairs[i][1];
        partner[a] = b;
        partner[b] = a;
    }
    int unhappy = 0;
    for (int x = 0; x < n; x++) {
        int y = partner[x];
        int limit = rank[x][y];
        for (int i = 0; i < limit; i++) {
            int u = preferences[x][i];
            if (rank[u][x] < rank[u][partner[u]]) {
                unhappy++;
                break;
            }
        }
    }
    for (int i = 0; i < n; i++) free(rank[i]);
    free(rank); free(partner);
    return unhappy;
}
