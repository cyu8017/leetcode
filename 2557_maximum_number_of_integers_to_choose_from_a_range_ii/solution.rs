// LeetCode 2557 - Maximum Number of Integers to Choose From a Range II
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-ii/

impl Solution {
    pub fn max_count(mut banned: Vec<i32>, n: i32, max_sum: i64) -> i32 {
        banned.sort_unstable();
        let mut uniq = Vec::new();
        for x in banned {
            if x >= 1 && x <= n && (uniq.is_empty() || *uniq.last().unwrap() != x) {
                uniq.push(x);
            }
        }
        let mut ans = 0i32;
        let mut prev = 0i32;
        let mut remain = max_sum;
        let mut check = |l: i64, r: i64, remain: &mut i64, ans: &mut i32| {
            if l > r || *remain <= 0 {
                return;
            }
            let mut lo = l;
            let mut hi = r;
            let mut best = l - 1;
            while lo <= hi {
                let mid = (lo + hi) / 2;
                let cnt = mid - l + 1;
                let sum = (l + mid) * cnt / 2;
                if sum <= *remain {
                    best = mid;
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }
            if best >= l {
                let cnt = (best - l + 1) as i32;
                *ans += cnt;
                *remain -= (l + best) * cnt as i64 / 2;
            }
        };
        for b in uniq {
            check(prev as i64 + 1, b as i64 - 1, &mut remain, &mut ans);
            prev = b;
        }
        check(prev as i64 + 1, n as i64, &mut remain, &mut ans);
        ans
    }
}
