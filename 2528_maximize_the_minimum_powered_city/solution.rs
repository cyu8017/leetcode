// LeetCode 2528 - Maximize the Minimum Powered City
// https://leetcode.com/problems/maximize-the-minimum-powered-city/

impl Solution {
    pub fn max_power(stations: Vec<i32>, r: i32, k: i32) -> i64 {
        let n = stations.len();
        let r = r as usize;
        let k = k as i64;
        let mut diff = vec![0i64; n + 1];
        for i in 0..n {
            let l = i.saturating_sub(r);
            let rr = (i + r).min(n - 1);
            diff[l] += stations[i] as i64;
            diff[rr + 1] -= stations[i] as i64;
        }
        let mut power = vec![0i64; n];
        let mut cur = 0i64;
        for i in 0..n {
            cur += diff[i];
            power[i] = cur;
        }
        let ok = |x: i64| -> bool {
            let mut extra = vec![0i64; n + 1];
            let mut have = 0i64;
            let mut used = 0i64;
            for i in 0..n {
                have += extra[i];
                let need = x - (power[i] + have);
                if need > 0 {
                    used += need;
                    if used > k {
                        return false;
                    }
                    have += need;
                    let end = i + 2 * r;
                    if end + 1 <= n {
                        extra[end + 1] -= need;
                    }
                }
            }
            true
        };
        let mut lo = 0i64;
        let mut hi = k;
        for &p in &power {
            if p > hi {
                hi = p;
            }
        }
        hi += k;
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if ok(mid) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        lo
    }
}
