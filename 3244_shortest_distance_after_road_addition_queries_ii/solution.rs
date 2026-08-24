// LeetCode 3244 - Shortest Distance After Road Addition Queries II
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/

impl Solution {
    pub fn shortest_distance_after_queries(n: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut nxt: Vec<i32> = (1..n as i32).collect();
        let mut cnt = n as i32 - 1;
        let mut ans = Vec::new();
        for q in queries {
            let u = q[0] as usize;
            let v = q[1];
            if nxt[u] > 0 && nxt[u] < v {
                let mut i = nxt[u];
                while i < v {
                    cnt -= 1;
                    let ni = nxt[i as usize];
                    nxt[i as usize] = 0;
                    i = ni;
                }
                nxt[u] = v;
            }
            ans.push(cnt);
        }
        ans
    }
}
