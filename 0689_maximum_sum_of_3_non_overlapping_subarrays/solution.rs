// LeetCode 0689 - Maximum Sum of 3 Non-Overlapping Subarrays
// https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

impl Solution {
    pub fn max_sum_of_three_subarrays(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        let k = k as usize;
        let windows = n - k + 1;
        let mut sums = vec![0; windows];
        let mut total: i32 = nums[..k].iter().sum();
        sums[0] = total;
        for i in 1..windows {
            total += nums[i + k - 1] - nums[i - 1];
            sums[i] = total;
        }

        let mut left = vec![0; windows];
        let mut best = 0;
        for i in 0..windows {
            if sums[i] > sums[best] {
                best = i;
            }
            left[i] = best;
        }

        let mut right = vec![0; windows];
        best = windows - 1;
        for i in (0..windows).rev() {
            if sums[i] >= sums[best] {
                best = i;
            }
            right[i] = best;
        }

        let mut answer = vec![0, 0, 0];
        let mut best_total = -1;
        for mid in k..windows - k {
            let l = left[mid - k];
            let r = right[mid + k];
            let cur = sums[l] + sums[mid] + sums[r];
            if cur > best_total {
                best_total = cur;
                answer = vec![l as i32, mid as i32, r as i32];
            }
        }
        answer
    }
}
