// LeetCode 3574 - Maximize Subarray GCD Score
// https://leetcode.com/problems/maximize-subarray-gcd-score/

fn gcd(mut a: i32, mut b: i32) -> i32 {
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a.abs()
}

impl Solution {
    pub fn max_gcd_score(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let mut cnt = vec![0i32; n];
        for i in 0..n {
            let mut x = nums[i];
            while x % 2 == 0 {
                cnt[i] += 1;
                x /= 2;
            }
        }
        let mut ans = 0i64;
        for l in 0..n {
            let mut g = 0;
            let mut mi = i32::MAX;
            let mut t = 0;
            for r in l..n {
                g = gcd(g, nums[r]);
                if cnt[r] < mi {
                    mi = cnt[r];
                    t = 1;
                } else if cnt[r] == mi {
                    t += 1;
                }
                let mut score = g as i64 * (r - l + 1) as i64;
                if t <= k {
                    score *= 2;
                }
                ans = ans.max(score);
            }
        }
        ans
    }
}
