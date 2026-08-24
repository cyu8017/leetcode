// LeetCode 3187 - Peaks in Array
// https://leetcode.com/problems/peaks-in-array/

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
    pub fn count_of_peaks(mut nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = nums.len();
        let mut tree = Bit::new(n.saturating_sub(1));
        let update = |tree: &mut Bit, nums: &[i32], i: i32, val: i32| {
            if i <= 0 || i >= n as i32 - 1 {
                return;
            }
            let i = i as usize;
            if nums[i - 1] < nums[i] && nums[i] > nums[i + 1] {
                tree.update(i, val);
            }
        };
        for i in 1..n.saturating_sub(1) {
            update(&mut tree, &nums, i as i32, 1);
        }
        let mut ans = Vec::new();
        for q in queries {
            if q[0] == 1 {
                let l = q[1] + 1;
                let r = q[2] - 1;
                let t = if l <= r {
                    tree.query(r as usize) - tree.query((l - 1) as usize)
                } else {
                    0
                };
                ans.push(t);
            } else {
                let idx = q[1];
                let val = q[2];
                for i in idx - 1..=idx + 1 {
                    update(&mut tree, &nums, i, -1);
                }
                nums[idx as usize] = val;
                for i in idx - 1..=idx + 1 {
                    update(&mut tree, &nums, i, 1);
                }
            }
        }
        ans
    }
}
