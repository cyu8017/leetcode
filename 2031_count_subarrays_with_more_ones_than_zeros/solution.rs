// LeetCode 2031 - Count Subarrays With More Ones Than Zeros
// https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/

struct Fenwick {
    bit: Vec<i32>,
}

impl Fenwick {
    fn new(n: usize) -> Self {
        Self { bit: vec![0; n + 2] }
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
    pub fn subarrays_with_more_zeros_than_ones(nums: Vec<i32>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let n = nums.len() as i32;
        let offset = n + 1;
        let mut fw = Fenwick::new((2 * n + 5) as usize);
        let mut pref = 0;
        let mut ans = 0;
        fw.add(offset as usize, 1);
        for x in nums {
            pref += if x == 1 { 1 } else { -1 };
            let idx = (pref + offset) as usize;
            ans = (ans + fw.sum(idx - 1)) % MOD;
            fw.add(idx, 1);
        }
        ans
    }
}
