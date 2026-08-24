// LeetCode 0845 - Longest Mountain in Array
// https://leetcode.com/problems/longest-mountain-in-array/

impl Solution {
    pub fn longest_mountain(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        let mut ans = 0;
        let mut i = 0;
        while i < n {
            let mut j = i;
            if j + 1 < n && arr[j] < arr[j + 1] {
                while j + 1 < n && arr[j] < arr[j + 1] {
                    j += 1;
                }
                if j + 1 < n && arr[j] > arr[j + 1] {
                    while j + 1 < n && arr[j] > arr[j + 1] {
                        j += 1;
                    }
                    ans = ans.max(j - i + 1);
                    i = j;
                    continue;
                }
            }
            i += 1;
        }
        ans as i32
    }
}
