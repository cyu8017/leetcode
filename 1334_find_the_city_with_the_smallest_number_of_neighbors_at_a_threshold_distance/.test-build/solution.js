"use strict";
// LeetCode 1334 - Find The City With The Smallest Number Of Neighbors At A Threshold Distance
// https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
function findTheCity(n, edges, distanceThreshold) {
    const inf = 1e15;
    const dist = Array.from({ length: n }, (), any), any;
    Array(n).fill(inf);
    ;
    for (let i = 0; i < n; i++)
        dist[i][i] = 0;
    for (const [a, b, weight] of edges) {
        dist[a][b] = dist[b][a] = weight;
    }
    for (let k = 0; k < n; k++) {
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < n; j++) {
                dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }
    let bestCity = 0, bestCount = n;
    for (let city = 0; city < n; city++) {
        const count = dist[city].filter((d) => d <= distanceThreshold).length;
        if (count < bestCount || (count === bestCount && city > bestCity)) {
            bestCount = count;
            bestCity = city;
        }
    }
    return bestCity;
}
