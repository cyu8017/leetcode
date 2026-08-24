// LeetCode 3022 - Minimize OR of Remaining Elements Using Operations
// https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/

impl Solution {
    pub fn min_or_after_operations(nums: Vec<i32>, k: i32) -> i32 {
        let mut ans = 0;
        let mut rans = 0;
        for i in (0..=29).rev() {
            let test = ans + (1 << i);
            let mut cnt = 0;
            let mut val = 0;
            for &num in &nums {
                if val == 0 {
                    val = test & num;
                } else {
                    val &= test & num;
                }
                if val != 0 {
                    cnt += 1;
                }
            }
            if cnt > k {
                rans += 1 << i;
            } else {
                ans += 1 << i;
            }
        }
        rans
    }
}
