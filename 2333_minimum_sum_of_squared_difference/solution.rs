// LeetCode 2333 - Minimum Sum of Squared Difference
// https://leetcode.com/problems/minimum-sum-of-squared-difference/

impl Solution {
    pub fn min_sum_square_diff(nums1: Vec<i32>, nums2: Vec<i32>, k1: i32, k2: i32) -> i64 {
        let n = nums1.len();
        let mut max_d = 0i32;
        let mut diff = vec![0i32; n];
        for i in 0..n {
            let d = (nums1[i] - nums2[i]).abs();
            diff[i] = d;
            if d > max_d {
                max_d = d;
            }
        }
        let mut k = k1 + k2;
        let mut freq = vec![0i32; (max_d + 1) as usize];
        for d in diff {
            freq[d as usize] += 1;
        }
        let mut d = max_d;
        while d > 0 && k > 0 {
            if freq[d as usize] != 0 {
                let mut take = freq[d as usize];
                if take > k {
                    take = k;
                }
                freq[d as usize] -= take;
                freq[(d - 1) as usize] += take;
                k -= take;
            }
            d -= 1;
        }
        let mut ans = 0i64;
        for d in 0..=max_d as usize {
            ans += d as i64 * d as i64 * freq[d] as i64;
        }
        ans
    }
}
