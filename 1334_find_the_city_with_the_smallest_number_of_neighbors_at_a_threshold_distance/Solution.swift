// LeetCode 1334 - Find the City With the Smallest Number of Neighbors at a Threshold Distance
// https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution {
    func findTheCity(_ n: Int, _ edges: [[Int]], _ distanceThreshold: Int) -> Int {
        let inf = Int.max / 4
        var dist = Array(repeating: Array(repeating: inf, count: n), count: n)
        for i in 0..<n { dist[i][i] = 0 }
        for e in edges {
            dist[e[0]][e[1]] = e[2]
            dist[e[1]][e[0]] = e[2]
        }
        for k in 0..<n {
            for i in 0..<n {
                for j in 0..<n {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                }
            }
        }
        var bestCity = 0, bestCount = Int.max
        for city in 0..<n {
            let count = dist[city].filter { $0 <= distanceThreshold }.count
            if count < bestCount || (count == bestCount && city > bestCity) {
                bestCount = count; bestCity = city
            }
        }
        return bestCity
    }
}
