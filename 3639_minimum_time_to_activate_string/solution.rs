// LeetCode 3639 - Minimum Time to Activate String
// https://leetcode.com/problems/minimum-time-to-activate-string/

impl Solution {
    pub fn min_time(s: String, order: Vec<i32>, k: i32) -> i32 {
        let n = s.len();
        let total = n as i64 * (n as i64 + 1) / 2;
        if k as i64 > total {
            return -1;
        }
        let count_valid = |t: i32| -> i64 {
            let mut star = vec![false; n];
            for i in 0..=t as usize {
                star[order[i] as usize] = true;
            }
            let mut invalid = 0i64;
            let mut i = 0;
            while i < n {
                if star[i] {
                    i += 1;
                    continue;
                }
                let mut j = i;
                while j < n && !star[j] {
                    j += 1;
                }
                let l = (j - i) as i64;
                invalid += l * (l + 1) / 2;
                i = j;
            }
            total - invalid
        };
        let mut lo = 0;
        let mut hi = n as i32 - 1;
        let mut ans = -1;
        while lo <= hi {
            let mid = (lo + hi) / 2;
            if count_valid(mid) >= k as i64 {
                ans = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        ans
    }
}
