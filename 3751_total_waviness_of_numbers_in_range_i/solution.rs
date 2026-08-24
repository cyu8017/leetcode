// LeetCode 3751 - Total Waviness Of Numbers In Range I
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/

impl Solution {
    fn f(mut x: i32) -> i32 {
        let mut nums = Vec::new();
        while x > 0 {
            nums.push(x % 10);
            x /= 10;
        }
        let m = nums.len();
        if m < 3 {
            return 0;
        }
        let mut s = 0;
        for i in 1..m - 1 {
            if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1])
                || (nums[i] < nums[i - 1] && nums[i] < nums[i + 1])
            {
                s += 1;
            }
        }
        s
    }

    pub fn total_waviness(num1: i32, num2: i32) -> i32 {
        let mut ans = 0;
        for x in num1..=num2 {
            ans += Self::f(x);
        }
        ans
    }
}
