// LeetCode 0787 - Cheapest Flights Within K Stops
// https://leetcode.com/problems/cheapest-flights-within-k-stops/

impl Solution {
    pub fn find_cheapest_price(n: i32, flights: Vec<Vec<i32>>, src: i32, dst: i32, k: i32) -> i32 {
        const INF: i32 = i32::MAX / 4;
        let n = n as usize;
        let mut dist = vec![INF; n];
        dist[src as usize] = 0;
        for _ in 0..=k {
            let mut nxt = dist.clone();
            for flight in &flights {
                let u = flight[0] as usize;
                let v = flight[1] as usize;
                let price = flight[2];
                if dist[u] != INF && dist[u] + price < nxt[v] {
                    nxt[v] = dist[u] + price;
                }
            }
            dist = nxt;
        }
        if dist[dst as usize] == INF {
            -1
        } else {
            dist[dst as usize]
        }
    }
}
