// LeetCode 2835 - Minimum Operations to Form Subsequence With Target Sum
// https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/

impl Solution {
    pub fn min_operations(nums: Vec<i32>, target: i32) -> i32 {
        let mut cnt = [0i32; 32];
        let mut sum = 0i64;
        for &v in &nums {
            sum += v as i64;
            let mut b = 0;
            while (1 << b) < v {
                b += 1;
            }
            cnt[b as usize] += 1;
        }
        if sum < target as i64 {
            return -1;
        }
        let mut ans = 0i32;
        for i in 0..31 {
            if (target & (1 << i)) != 0 {
                if cnt[i] > 0 {
                    cnt[i] -= 1;
                } else {
                    let mut j = i + 1;
                    while j < 32 && cnt[j] == 0 {
                        j += 1;
                    }
                    if j == 32 {
                        return -1;
                    }
                    while j > i {
                        cnt[j] -= 1;
                        cnt[j - 1] += 2;
                        ans += 1;
                        j -= 1;
                    }
                    cnt[i] -= 1;
                }
            }
            cnt[i + 1] += cnt[i] / 2;
        }
        ans
    }
}
