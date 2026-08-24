// LeetCode 3739 - Count Subarrays With Majority Element II
// https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

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
        let mut s = 0;
        while x > 0 {
            s += self.c[x];
            x -= x & x.wrapping_neg();
        }
        s
    }
}

impl Solution {
    pub fn count_majority_subarrays(nums: Vec<i32>, target: i32) -> i64 {
        let n = nums.len();
        let mut tree = Bit::new(2 * n + 1);
        let mut s = n + 1;
        tree.update(s, 1);
        let mut ans = 0i64;
        for x in nums {
            if x == target {
                s += 1;
            } else {
                s -= 1;
            }
            ans += tree.query(s - 1) as i64;
            tree.update(s, 1);
        }
        ans
    }
}
