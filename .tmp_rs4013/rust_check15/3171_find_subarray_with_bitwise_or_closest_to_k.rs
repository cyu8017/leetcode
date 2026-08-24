struct Solution;
// LeetCode 3171 - Find Subarray With Bitwise OR Closest to K
// https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/

impl Solution {
    pub fn minimum_difference(nums: Vec<i32>, k: i32) -> i32 {
        let mx = *nums.iter().max().unwrap();
        let m = if mx == 0 { 1 } else { 32 - mx.leading_zeros() as i32 };
        let mut cnt = vec![0; m as usize];
        let mut ans = i32::MAX;
        let mut s = 0;
        let mut i = 0;
        for j in 0..nums.len() {
            let x = nums[j];
            s |= x;
            ans = ans.min((s - k).abs());
            for h in 0..m {
                if (x >> h) & 1 == 1 {
                    cnt[h as usize] += 1;
                }
            }
            while i < j && s > k {
                let y = nums[i];
                for h in 0..m {
                    if (y >> h) & 1 == 1 {
                        cnt[h as usize] -= 1;
                        if cnt[h as usize] == 0 {
                            s ^= 1 << h;
                        }
                    }
                }
                ans = ans.min((s - k).abs());
                i += 1;
            }
        }
        ans
    }
}

fn main() {}
