// LeetCode 1334 - Find the City With the Smallest Number of Neighbors at a Threshold Distance
// https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

impl Solution {
    pub fn find_the_city(n: i32, edges: Vec<Vec<i32>>, distance_threshold: i32) -> i32 {
        let n = n as usize;
        let inf = i64::MAX / 4;
        let mut dist = vec![vec![inf; n]; n];
        for i in 0..n {
            dist[i][i] = 0;
        }
        for e in edges {
            let (a, b, w) = (e[0] as usize, e[1] as usize, e[2] as i64);
            dist[a][b] = w;
            dist[b][a] = w;
        }
        for k in 0..n {
            for i in 0..n {
                for j in 0..n {
                    dist[i][j] = dist[i][j].min(dist[i][k] + dist[k][j]);
                }
            }
        }
        (0..n)
            .min_by_key(|&city| {
                (
                    dist[city]
                        .iter()
                        .filter(|&&d| d <= distance_threshold as i64)
                        .count(),
                    -(city as i32),
                )
            })
            .unwrap() as i32
    }
}
