// LeetCode 1643 - Kth Smallest Instructions
// https://leetcode.com/problems/kth-smallest-instructions/

impl Solution {
    pub fn kth_smallest_path(destination: Vec<i32>, mut k: i32) -> String {
        let (mut v, mut h) = (destination[0], destination[1]);
        let mut ans = String::new();
        while h + v > 0 {
            if h > 0 {
                let count = Self::comb(h + v - 1, v);
                if k <= count {
                    ans.push('H');
                    h -= 1;
                    continue;
                }
                k -= count;
            }
            ans.push('V');
            v -= 1;
        }
        ans
    }

    fn comb(n: i32, mut r: i32) -> i32 {
        if r < 0 || r > n {
            return 0;
        }
        if r > n - r {
            r = n - r;
        }
        let mut res = 1i64;
        for i in 0..r {
            res = res * (n - i) as i64 / (i + 1) as i64;
        }
        res as i32
    }
}
