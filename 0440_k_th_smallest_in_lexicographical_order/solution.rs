// LeetCode 0440 - K-th Smallest in Lexicographical Order
// https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

impl Solution {
    fn count_steps(n: i32, mut first: i64, mut last: i64) -> i64 {
        let mut steps = 0;
        while first <= i64::from(n) {
            steps += i64::min(i64::from(n) + 1, last) - first;
            first *= 10;
            last *= 10;
        }
        steps
    }

    pub fn find_kth_number(n: i32, k: i32) -> i32 {
        let mut current = 1i64;
        let mut remaining = i64::from(k) - 1;

        while remaining > 0 {
            let steps = Self::count_steps(n, current, current + 1);
            if steps <= remaining {
                current += 1;
                remaining -= steps;
            } else {
                current *= 10;
                remaining -= 1;
            }
        }

        current as i32
    }
}
