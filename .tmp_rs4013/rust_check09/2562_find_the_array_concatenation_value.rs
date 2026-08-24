struct Solution;

// LeetCode 2562 - Find the Array Concatenation Value
// https://leetcode.com/problems/find-the-array-concatenation-value/

impl Solution {
    pub fn find_the_array_conc_val(nums: Vec<i32>) -> i64 {
        let mut ans = 0i64;
        let mut l = 0;
        let mut r = nums.len() as i32 - 1;
        while l <= r {
            if l == r {
                ans += nums[l as usize] as i64;
                break;
            }
            let left = nums[l as usize];
            let right = nums[r as usize];
            let mut pow = 1i64;
            let mut t = right;
            while t > 0 {
                pow *= 10;
                t /= 10;
            }
            ans += left as i64 * pow + right as i64;
            l += 1;
            r -= 1;
        }
        ans
    }
}

fn main() {}
