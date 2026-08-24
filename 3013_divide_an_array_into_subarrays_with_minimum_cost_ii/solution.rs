// LeetCode 3013 - Divide an Array Into Subarrays With Minimum Cost II
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/

struct Biti {
    n: usize,
    c: Vec<i32>,
}
impl Biti {
    fn new(n: usize) -> Self {
        Self { n, c: vec![0; n + 1] }
    }
    fn upd(&mut self, mut x: usize, d: i32) {
        while x <= self.n {
            self.c[x] += d;
            x += x & x.wrapping_neg();
        }
    }
    fn qry(&self, mut x: usize) -> i32 {
        let mut s = 0;
        while x > 0 {
            s += self.c[x];
            x -= x & x.wrapping_neg();
        }
        s
    }
}

struct Bitl {
    n: usize,
    c: Vec<i64>,
}
impl Bitl {
    fn new(n: usize) -> Self {
        Self { n, c: vec![0; n + 1] }
    }
    fn upd(&mut self, mut x: usize, d: i64) {
        while x <= self.n {
            self.c[x] += d;
            x += x & x.wrapping_neg();
        }
    }
    fn qry(&self, mut x: usize) -> i64 {
        let mut s = 0i64;
        while x > 0 {
            s += self.c[x];
            x -= x & x.wrapping_neg();
        }
        s
    }
}

impl Solution {
    pub fn minimum_cost(nums: Vec<i32>, k: i32, dist: i32) -> i64 {
        let mut k = k - 1;
        let n = nums.len();
        let mut uniq = nums.clone();
        uniq.sort_unstable();
        uniq.dedup();
        let m = uniq.len();
        let mut cnt = Biti::new(m + 2);
        let mut sum = Bitl::new(m + 2);
        let rank = |uniq: &[i32], x: i32| -> usize {
            uniq.binary_search(&x).unwrap_or_else(|e| e) + 1
        };
        let add_val = |cnt: &mut Biti, sum: &mut Bitl, uniq: &[i32], x: i32, d: i32| {
            let r = rank(uniq, x);
            cnt.upd(r, d);
            sum.upd(r, d as i64 * x as i64);
        };
        let kth = |cnt: &Biti, m: usize, mut kk: i32| -> usize {
            let mut idx = 0usize;
            let mut bit = 1usize << 20;
            while bit > 0 {
                let nidx = idx + bit;
                if nidx <= m && cnt.c[nidx] < kk {
                    kk -= cnt.c[nidx];
                    idx = nidx;
                }
                bit >>= 1;
            }
            idx + 1
        };
        let sum_smallest = |cnt: &Biti, sum: &Bitl, uniq: &[i32], kk: i32| -> i64 {
            if kk <= 0 {
                return 0;
            }
            let r = kth(cnt, m, kk);
            let before = cnt.qry(r - 1);
            let mut s = sum.qry(r - 1);
            s += (kk - before) as i64 * uniq[r - 1] as i64;
            s
        };
        let end = (dist as usize + 1).min(n - 1);
        for i in 1..=end {
            add_val(&mut cnt, &mut sum, &uniq, nums[i], 1);
        }
        let mut kk = k.min(end as i32);
        let mut ans = nums[0] as i64 + sum_smallest(&cnt, &sum, &uniq, kk);
        let start = dist as usize + 2;
        for i in start..n {
            add_val(&mut cnt, &mut sum, &uniq, nums[i - dist as usize - 1], -1);
            add_val(&mut cnt, &mut sum, &uniq, nums[i], 1);
            kk = k.min(dist + 1);
            ans = ans.min(nums[0] as i64 + sum_smallest(&cnt, &sum, &uniq, kk));
        }
        let _ = k;
        ans
    }
}
