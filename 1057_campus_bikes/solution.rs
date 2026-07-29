// LeetCode 1057 - Campus Bikes
// https://leetcode.com/problems/campus-bikes/

impl Solution {
    pub fn assign_bikes(workers: Vec<Vec<i32>>, bikes: Vec<Vec<i32>>) -> Vec<i32> {
        let mut triples = Vec::new();
        for (w, worker) in workers.iter().enumerate() {
            for (b, bike) in bikes.iter().enumerate() {
                let dist = (worker[0] - bike[0]).abs() + (worker[1] - bike[1]).abs();
                triples.push((dist, w, b));
            }
        }
        triples.sort_unstable();
        let mut ans = vec![-1; workers.len()];
        let mut used_bikes = vec![false; bikes.len()];
        let mut assigned = 0;
        for (_, w, b) in triples {
            if ans[w] == -1 && !used_bikes[b] {
                ans[w] = b as i32;
                used_bikes[b] = true;
                assigned += 1;
                if assigned == workers.len() {
                    break;
                }
            }
        }
        ans
    }
}
