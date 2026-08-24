// LeetCode 3911 - K-th Smallest Remaining Even Integer in Subarray Queries
// https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/

impl Solution {
    pub fn kth_smallest_even(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i64> {
        let n = nums.len();
        let mut even_prefix = vec![0; n + 1];
        for i in 0..n {
            even_prefix[i + 1] = even_prefix[i] + if nums[i] % 2 == 0 { 1 } else { 0 };
        }
        let mut ans = vec![0i64; queries.len()];
        for (qi, q) in queries.iter().enumerate() {
            let l = q[0] as usize;
            let r = q[1] as usize;
            let k = q[2] as i64;
            let mut lo = 1i64;
            let mut hi = k + (r - l + 1) as i64;
            while lo < hi {
                let mid = (lo + hi) / 2;
                let mut pos = nums.partition_point(|&v| v <= (2 * mid) as i32);
                if pos > r + 1 {
                    pos = r + 1;
                }
                let mut removed = 0;
                if pos > l {
                    removed = even_prefix[pos] - even_prefix[l];
                }
                if mid - removed as i64 >= k {
                    hi = mid;
                } else {
                    lo = mid + 1;
                }
            }
            ans[qi] = 2 * lo;
        }
        ans
    }
}
