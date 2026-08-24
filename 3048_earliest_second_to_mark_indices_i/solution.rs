// LeetCode 3048 - Earliest Second to Mark Indices I
// https://leetcode.com/problems/earliest-second-to-mark-indices-i/

impl Solution {
    pub fn earliest_second_to_mark_indices(nums: Vec<i32>, change_indices: Vec<i32>) -> i32 {
        let n = nums.len();
        let m = change_indices.len();
        let ok = |t: usize| -> bool {
            let mut last = vec![0usize; n + 1];
            for s in 0..t {
                last[change_indices[s] as usize] = s;
            }
            let mut decrement = 0i32;
            let mut marked = 0usize;
            for s in 0..t {
                let i = change_indices[s] as usize;
                if last[i] == s {
                    if decrement < nums[i - 1] {
                        return false;
                    }
                    decrement -= nums[i - 1];
                    marked += 1;
                } else {
                    decrement += 1;
                }
            }
            marked == n
        };
        let mut l = 0usize;
        let mut r = m + 1;
        while l < r {
            let mid = (l + r) / 2;
            if ok(mid) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        if l > m { -1 } else { l as i32 }
    }
}
