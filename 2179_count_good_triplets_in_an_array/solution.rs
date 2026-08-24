// LeetCode 2179 - Count Good Triplets in an Array
// https://leetcode.com/problems/count-good-triplets-in-an-array/

struct Fenwick {
    bit: Vec<i32>,
}

impl Fenwick {
    fn new(n: usize) -> Self {
        Self { bit: vec![0; n] }
    }
    fn add(&mut self, mut i: usize, v: i32) {
        while i < self.bit.len() {
            self.bit[i] += v;
            i += i & i.wrapping_neg();
        }
    }
    fn sum(&self, mut i: usize) -> i32 {
        let mut s = 0;
        while i > 0 {
            s += self.bit[i];
            i -= i & i.wrapping_neg();
        }
        s
    }
}

impl Solution {
    pub fn good_triplets(nums1: Vec<i32>, nums2: Vec<i32>) -> i64 {
        let n = nums1.len();
        let mut pos2 = vec![0; n];
        for i in 0..n {
            pos2[nums2[i] as usize] = i;
        }
        let mapped: Vec<usize> = nums1.iter().map(|&x| pos2[x as usize]).collect();
        let mut left = vec![0i32; n];
        let mut right = vec![0i32; n];
        let mut fw = Fenwick::new(n + 2);
        for i in 0..n {
            left[i] = fw.sum(mapped[i]);
            fw.add(mapped[i] + 1, 1);
        }
        fw = Fenwick::new(n + 2);
        for i in (0..n).rev() {
            right[i] = fw.sum(n) - fw.sum(mapped[i] + 1);
            fw.add(mapped[i] + 1, 1);
        }
        (0..n).map(|i| left[i] as i64 * right[i] as i64).sum()
    }
}
