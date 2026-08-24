// LeetCode 3116 - Kth Smallest Amount With Single Denomination Combination
// https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/

impl Solution {
    fn gcdll(mut a: i64, mut b: i64) -> i64 {
        while b != 0 {
            let t = a % b;
            a = b;
            b = t;
        }
        a
    }
    fn lcmll(a: i64, b: i64) -> i64 {
        a / Self::gcdll(a, b) * b
    }

    pub fn find_kth_smallest(coins: Vec<i32>, k: i32) -> i64 {
        let r = 100_000_000_000i64;
        let n = coins.len();
        let check = |mx: i64| -> bool {
            let mut cnt = 0i64;
            for i in 1..(1 << n) {
                let mut v = 1i64;
                for j in 0..n {
                    if (i >> j) & 1 == 1 {
                        v = Self::lcmll(v, coins[j] as i64);
                        if v > mx {
                            break;
                        }
                    }
                }
                let m = i.count_ones();
                if m % 2 == 1 {
                    cnt += mx / v;
                } else {
                    cnt -= mx / v;
                }
            }
            cnt >= k as i64
        };
        let mut lo = 1i64;
        let mut hi = r;
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if check(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
