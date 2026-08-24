// LeetCode 0719 - Find K-th Smallest Pair Distance
// https://leetcode.com/problems/find-k-th-smallest-pair-distance/

impl Solution {
    pub fn smallest_distance_pair(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort_unstable();
        let mut lo = 0;
        let mut hi = nums[nums.len() - 1] - nums[0];
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if Self::count_pairs(&nums, mid) >= k {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }

    fn count_pairs(nums: &[i32], distance: i32) -> i32 {
        let mut count = 0;
        let mut left = 0;
        for right in 0..nums.len() {
            while nums[right] - nums[left] > distance {
                left += 1;
            }
            count += (right - left) as i32;
        }
        count
    }
}
