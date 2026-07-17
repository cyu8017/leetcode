// LeetCode 1703 - Minimum Adjacent Swaps for K Consecutive Ones
// https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/

impl Solution {
    pub fn min_moves(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let mut adjusted: Vec<i64> = Vec::new();
        for (i, &v) in nums.iter().enumerate() {
            if v == 1 {
                adjusted.push(i as i64 - adjusted.len() as i64);
            }
        }
        let m = adjusted.len();
        let mut prefix = vec![0i64; m + 1];
        for i in 0..m {
            prefix[i + 1] = prefix[i] + adjusted[i];
        }
        let mut best = i64::MAX;
        for left in 0..=(m - k) {
            let right = left + k;
            let mid = left + k / 2;
            let median = adjusted[mid];
            let mut cost = median * (mid - left) as i64 - (prefix[mid] - prefix[left]);
            cost += (prefix[right] - prefix[mid + 1]) - median * (right - mid - 1) as i64;
            best = best.min(cost);
        }
        best as i32
    }
}
