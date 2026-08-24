// LeetCode 3119 - Maximum Number of Potholes That Can Be Fixed
// https://leetcode.com/problems/maximum-number-of-potholes-that-can-be-fixed/

impl Solution {
    pub fn max_potholes(road: String, mut budget: i32) -> i32 {
        let mut road = road.into_bytes();
        road.push(b'.');
        let n = road.len();
        let mut cnt = vec![0i32; n];
        let mut k = 0i32;
        let mut ans = 0i32;
        for &c in &road {
            if c == b'x' {
                k += 1;
            } else if k > 0 {
                cnt[k as usize] += 1;
                k = 0;
            }
        }
        k = n as i32 - 1;
        while k > 0 && budget > 0 {
            let t = (budget / (k + 1)).min(cnt[k as usize]);
            ans += t * k;
            budget -= t * (k + 1);
            cnt[(k - 1) as usize] += cnt[k as usize] - t;
            k -= 1;
        }
        ans
    }
}
