// LeetCode 2959 - Number of Possible Sets of Closing Branches
// https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/

impl Solution {
    pub fn number_of_sets(n: i32, max_distance: i32, roads: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut ans = 0;
        for mask in 0..(1 << n) {
            let mut dist = vec![vec![1 << 29; n]; n];
            for i in 0..n {
                dist[i][i] = 0;
            }
            for r in &roads {
                let u = r[0] as usize;
                let v = r[1] as usize;
                let w = r[2];
                if (mask & (1 << u)) != 0 && (mask & (1 << v)) != 0 && w < dist[u][v] {
                    dist[u][v] = w;
                    dist[v][u] = w;
                }
            }
            for k in 0..n {
                if (mask & (1 << k)) == 0 {
                    continue;
                }
                for i in 0..n {
                    if (mask & (1 << i)) == 0 {
                        continue;
                    }
                    for j in 0..n {
                        if (mask & (1 << j)) == 0 {
                            continue;
                        }
                        if dist[i][k] + dist[k][j] < dist[i][j] {
                            dist[i][j] = dist[i][k] + dist[k][j];
                        }
                    }
                }
            }
            let mut ok = true;
            for i in 0..n {
                if (mask & (1 << i)) == 0 {
                    continue;
                }
                for j in 0..n {
                    if (mask & (1 << j)) == 0 {
                        continue;
                    }
                    if dist[i][j] > max_distance {
                        ok = false;
                        break;
                    }
                }
                if !ok {
                    break;
                }
            }
            if ok {
                ans += 1;
            }
        }
        ans
    }
}
