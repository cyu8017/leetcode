// LeetCode 2251 - Number of Flowers in Full Bloom
// https://leetcode.com/problems/number-of-flowers-in-full-bloom/

impl Solution {
    pub fn full_bloom_flowers(flowers: Vec<Vec<i32>>, people: Vec<i32>) -> Vec<i32> {
        let mut start = Vec::new();
        let mut end = Vec::new();
        for f in flowers {
            start.push(f[0]);
            end.push(f[1]);
        }
        start.sort_unstable();
        end.sort_unstable();
        let mut ans = vec![0; people.len()];
        for (i, &t) in people.iter().enumerate() {
            let started = start.partition_point(|&v| v <= t) as i32;
            let ended = end.partition_point(|&v| v < t) as i32;
            ans[i] = started - ended;
        }
        ans
    }
}
