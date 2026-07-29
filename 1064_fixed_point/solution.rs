// LeetCode 1064 - Fixed Point
// https://leetcode.com/problems/fixed-point/

impl Solution {
    pub fn fixed_point(arr: Vec<i32>) -> i32 {
        let mut lo = 0i32;
        let mut hi = arr.len() as i32 - 1;
        let mut ans = -1;
        while lo <= hi {
            let mid = (lo + hi) / 2;
            if arr[mid as usize] == mid {
                ans = mid;
                hi = mid - 1;
            } else if arr[mid as usize] < mid {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        ans
    }
}
