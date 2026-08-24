// LeetCode 3109 - Find the Index of Permutation
// https://leetcode.com/problems/find-the-index-of-permutation/

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
    pub fn get_permutation_index(perm: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = perm.len();
        let mut tree = Bit::new(n + 1);
        let mut f = vec![0i64; n];
        f[0] = 1;
        for i in 1..n {
            f[i] = f[i - 1] * i as i64 % MOD;
        }
        let mut ans = 0i64;
        for i in 0..n {
            let x = perm[i] as usize;
            let cnt = x as i64 - 1 - tree.query(x) as i64;
            ans = (ans + cnt * f[n - 1 - i]) % MOD;
            tree.update(x, 1);
        }
        ans as i32
    }
}
