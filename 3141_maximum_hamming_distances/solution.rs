// LeetCode 3141 - Maximum Hamming Distances
// https://leetcode.com/problems/maximum-hamming-distances/

impl Solution {
    pub fn max_hamming_distances(mut nums: Vec<i32>, m: i32) -> Vec<i32> {
        let m = m as usize;
        let mut dist = vec![-1i32; 1 << m];
        let mut q = Vec::new();
        for &x in &nums {
            dist[x as usize] = 0;
            q.push(x as usize);
        }
        let mut k = 1;
        while !q.is_empty() {
            let mut t = Vec::new();
            for &x in &q {
                for i in 0..m {
                    let y = x ^ (1 << i);
                    if dist[y] == -1 {
                        dist[y] = k;
                        t.push(y);
                    }
                }
            }
            q = t;
            k += 1;
        }
        let mask = (1 << m) - 1;
        for i in 0..nums.len() {
            let x = nums[i] as usize;
            nums[i] = m as i32 - dist[x ^ mask];
        }
        nums
    }
}
