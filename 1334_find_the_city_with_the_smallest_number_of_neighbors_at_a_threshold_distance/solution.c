// LeetCode 1334 - Find the City With the Smallest Number of Neighbors at a Threshold Distance
// https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

#include <stdlib.h>

int findTheCity(int n, int** edges, int edgesSize, int* edgesColSize, int distanceThreshold) {
    (void)edgesColSize;
    long long INF = 1000000000000000LL;
    long long* dist = (long long*)malloc(n * n * sizeof(long long));
    for (int i = 0; i < n * n; i++) dist[i] = INF;
    for (int i = 0; i < n; i++) dist[i * n + i] = 0;
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1], w = edges[i][2];
        dist[a * n + b] = dist[b * n + a] = w;
    }
    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (dist[i * n + k] + dist[k * n + j] < dist[i * n + j])
                    dist[i * n + j] = dist[i * n + k] + dist[k * n + j];
    int bestCity = 0, bestCount = n + 1;
    for (int city = 0; city < n; city++) {
        int count = 0;
        for (int j = 0; j < n; j++) if (dist[city * n + j] <= distanceThreshold) count++;
        if (count < bestCount || (count == bestCount && city > bestCity)) {
            bestCount = count;
            bestCity = city;
        }
    }
    free(dist);
    return bestCity;
}
