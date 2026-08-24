// LeetCode 3043 - Find the Length of the Longest Common Prefix
// https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

use std::collections::HashSet;

impl Solution {
    pub fn longest_common_prefix(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
        let mut s = HashSet::new();
        for mut x in arr1 {
            while x > 0 {
                s.insert(x);
                x /= 10;
            }
        }
        let mut mx = 0;
        for mut x in arr2 {
            while x > 0 {
                if s.contains(&x) {
                    mx = mx.max(x);
                    break;
                }
                x /= 10;
            }
        }
        if mx > 0 {
            mx.to_string().len() as i32
        } else {
            0
        }
    }
}
