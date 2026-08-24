struct Solution;
// LeetCode 3907 - Count Smaller Elements With Opposite Parity
// https://leetcode.com/problems/count-smaller-elements-with-opposite-parity/

struct Bit {
    n: usize,
    c: Vec<i32>,
}

impl Bit {
    fn new(n: usize) -> Self {
        Self { n, c: vec![0; n + 1] }
    }
    fn update(&mut self, mut x: usize, delta: i32) {
        while x <= self.n {
            self.c[x] += delta;
            x += x & x.wrapping_neg();
        }
    }
    fn query(&self, mut x: usize) -> i32 {
        let mut s = 0;
        while x > 0 {
            s += self.c[x];
            x -= x & x.wrapping_neg();
        }
        s
    }
}

impl Solution {
    pub fn count_smaller_opposite_parity(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut sorted = nums.clone();
        sorted.sort_unstable();
        sorted.dedup();
        let m = sorted.len();
        let mut bits = [Bit::new(m), Bit::new(m)];
        let mut ans = vec![0; n];
        for i in (0..n).rev() {
            let x = sorted.partition_point(|&v| v < nums[i]) + 1;
            ans[i] = bits[((nums[i] & 1) ^ 1) as usize].query(x - 1);
            bits[(nums[i] & 1) as usize].update(x, 1);
        }
        ans
    }
}
