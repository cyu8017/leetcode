// LeetCode 3097 - Shortest Subarray With OR at Least K II
// https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/

impl Solution {
    pub fn minimum_subarray_length(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut cnt = [0i32; 32];
        let mut ans = n as i32 + 1;
        let mut s = 0i32;
        let mut i = 0usize;
        for j in 0..n {
            let x = nums[j];
            s |= x;
            for h in 0..32 {
                if (x >> h) & 1 == 1 {
                    cnt[h] += 1;
                }
            }
            while s >= k && i <= j {
                ans = ans.min((j - i + 1) as i32);
                for h in 0..32 {
                    if (nums[i] >> h) & 1 == 1 {
                        cnt[h] -= 1;
                        if cnt[h] == 0 {
                            s ^= 1 << h;
                        }
                    }
                }
                i += 1;
            }
        }
        if ans == n as i32 + 1 { -1 } else { ans }
    }
}
