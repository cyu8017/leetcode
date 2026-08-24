// LeetCode 4013 - Count Subarrays With Even Odd Ratio II
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/

struct Bit {
    n: usize,
    c: Vec<i32>,
}

impl Bit {
    fn new(n: usize) -> Self {
        Self {
            n,
            c: vec![0; n + 1],
        }
    }

    fn update(&mut self, mut x: usize, delta: i32) {
        while x <= self.n {
            self.c[x] += delta;
            x += x & x.wrapping_neg();
        }
    }

    fn query(&self, mut x: usize) -> i32 {
        let mut sum = 0;
        while x > 0 {
            sum += self.c[x];
            x -= x & x.wrapping_neg();
        }
        sum
    }
}

impl Solution {
    pub fn count_ratio_subarrays(nums: Vec<i32>, a: i32, b: i32) -> i64 {
        let n = nums.len();
        let mut s = vec![0i64; n + 1];
        for i in 0..n {
            if nums[i] % 2 == 1 {
                s[i + 1] = s[i] + a as i64;
            } else {
                s[i + 1] = s[i] - b as i64;
            }
        }
        let mut st = s.clone();
        st.sort_unstable();
        st.dedup();
        let mut bit = Bit::new(st.len() + 1);
        let mut ans = 0i64;
        for &v in &s {
            let x = st.partition_point(|&z| z < v) + 1;
            ans += bit.query(x) as i64;
            bit.update(x, 1);
        }
        ans
    }
}
