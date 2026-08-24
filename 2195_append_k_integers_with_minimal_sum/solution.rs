// LeetCode 2195 - Append K Integers With Minimal Sum
// https://leetcode.com/problems/append-k-integers-with-minimal-sum/

impl Solution {
    pub fn minimal_k_sum(mut nums: Vec<i32>, mut k: i32) -> i64 {
        nums.sort_unstable();
        let mut ans: i64 = 0;
        let mut prev = 0i32;
        for x in nums {
            if x <= prev {
                continue;
            }
            let start = prev + 1;
            let mut end = x - 1;
            if start <= end {
                let mut cnt = end - start + 1;
                if cnt > k {
                    end = start + k - 1;
                    cnt = k;
                }
                ans += (start as i64 + end as i64) * cnt as i64 / 2;
                k -= cnt;
                if k == 0 {
                    return ans;
                }
            }
            prev = x;
        }
        let start = prev as i64 + 1;
        let end = start + k as i64 - 1;
        ans += (start + end) * k as i64 / 2;
        ans
    }
}
