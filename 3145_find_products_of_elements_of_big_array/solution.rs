// LeetCode 3145 - Find Products of Elements of Big Array
// https://leetcode.com/problems/find-products-of-elements-of-big-array/

impl Solution {
    fn init_tables() -> ([i64; 51], [i64; 51]) {
        let mut cnt = [0i64; 51];
        let mut s = [0i64; 51];
        let mut p = 1i64;
        for i in 1..=50 {
            cnt[i] = cnt[i - 1] * 2 + p;
            s[i] = s[i - 1] * 2 + p * (i as i64 - 1);
            p *= 2;
        }
        (cnt, s)
    }

    fn num_idx_and_sum(mut x: i64, cnt: &[i64; 51], s: &[i64; 51]) -> (i64, i64) {
        let mut idx = 0i64;
        let mut total_sum = 0i64;
        while x > 0 {
            let i = 63 - (x as u64).leading_zeros() as i32;
            idx += cnt[i as usize];
            total_sum += s[i as usize];
            x -= 1i64 << i;
            total_sum += (x + 1) * i as i64;
            idx += x + 1;
        }
        (idx, total_sum)
    }

    fn f(i: i64, cnt: &[i64; 51], s: &[i64; 51]) -> i64 {
        const M: i32 = 50;
        let mut l = 0i64;
        let mut r = 1i64 << M;
        while l < r {
            let mid = (l + r + 1) >> 1;
            let (idx, _) = Self::num_idx_and_sum(mid, cnt, s);
            if idx < i {
                l = mid;
            } else {
                r = mid - 1;
            }
        }
        let (idx, mut total_sum) = Self::num_idx_and_sum(l, cnt, s);
        let mut rem = i - idx;
        let mut x = l + 1;
        for _ in 0..rem {
            let y = x & x.wrapping_neg();
            total_sum += (y as u64).trailing_zeros() as i64;
            x -= y;
        }
        total_sum
    }

    fn qpow(mut a: i64, mut n: i64, modn: i64) -> i64 {
        let mut ans = 1 % modn;
        a %= modn;
        while n > 0 {
            if n & 1 == 1 {
                ans = ans * a % modn;
            }
            a = a * a % modn;
            n >>= 1;
        }
        ans
    }

    pub fn find_products_of_elements(queries: Vec<Vec<i64>>) -> Vec<i32> {
        let (cnt, s) = Self::init_tables();
        queries
            .iter()
            .map(|q| {
                let (left, right, modn) = (q[0], q[1], q[2]);
                let power = Self::f(right + 1, &cnt, &s) - Self::f(left, &cnt, &s);
                Self::qpow(2, power, modn) as i32
            })
            .collect()
    }
}
