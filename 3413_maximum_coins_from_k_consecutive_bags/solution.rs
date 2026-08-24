// LeetCode 3413 - Maximum Coins From K Consecutive Bags
// https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/

impl Solution {
    pub fn maximum_coins(mut coins: Vec<Vec<i32>>, k: i32) -> i64 {
        coins.sort_by_key(|a| a[0]);
        let mut ans = 0i64;
        let n = coins.len();
        for i in 0..n {
            let mut sum = 0i64;
            let start = coins[i][0];
            let end = start + k - 1;
            let mut j = i;
            while j < n && coins[j][0] <= end {
                let mut l = coins[j][0];
                let mut r = coins[j][1];
                if r > end {
                    r = end;
                }
                if l < start {
                    l = start;
                }
                if l <= r {
                    sum += (r - l + 1) as i64 * coins[j][2] as i64;
                }
                j += 1;
            }
            if sum > ans {
                ans = sum;
            }
        }
        for i in 0..n {
            let mut sum = 0i64;
            let end = coins[i][1];
            let start = end - k + 1;
            for j in 0..=i {
                let mut l = coins[j][0];
                let mut r = coins[j][1];
                if l < start {
                    l = start;
                }
                if r > end {
                    r = end;
                }
                if l <= r {
                    sum += (r - l + 1) as i64 * coins[j][2] as i64;
                }
            }
            if sum > ans {
                ans = sum;
            }
        }
        ans
    }
}
