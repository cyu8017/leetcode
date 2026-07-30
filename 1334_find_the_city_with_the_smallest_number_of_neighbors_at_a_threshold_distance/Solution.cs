// LeetCode 1334 - Find The City With The Smallest Number Of Neighbors At A Threshold Distance
// https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

public class Solution {
    public int FindTheCity(int n, int[][] edges, int distanceThreshold) {
        long inf = 1000000000000000L;
        var dist = new long[n, n];
        for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) dist[i, j] = i == j ? 0 : inf;
        foreach (var e in edges) { dist[e[0], e[1]] = e[2]; dist[e[1], e[0]] = e[2]; }
        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    if (dist[i, k] + dist[k, j] < dist[i, j]) dist[i, j] = dist[i, k] + dist[k, j];
        int bestCity = 0, bestCount = n;
        for (int city = 0; city < n; city++) {
            int count = 0;
            for (int j = 0; j < n; j++) if (dist[city, j] <= distanceThreshold) count++;
            if (count <= bestCount) { bestCount = count; bestCity = city; }
        }
        return bestCity;
    }
}
