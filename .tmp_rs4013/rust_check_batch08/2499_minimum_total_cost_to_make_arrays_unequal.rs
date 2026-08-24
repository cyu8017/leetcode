struct Solution;
// LeetCode 2499 - Minimum Total Cost to Make Arrays Unequal
// https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/

use std::collections::HashMap;

impl Solution {
    pub fn minimum_total_cost(nums1: Vec<i32>, nums2: Vec<i32>) -> i64 {
        let n = nums1.len();
        let mut freq: HashMap<i32, i32> = HashMap::new();
        let mut ans = 0i64;
        let mut same = 0;
        for i in 0..n {
            if nums1[i] == nums2[i] {
                same += 1;
                *freq.entry(nums1[i]).or_insert(0) += 1;
                ans += i as i64;
            }
        }
        let mut max_freq = 0;
        let mut max_val = 0;
        for (&v, &c) in &freq {
            if c > max_freq {
                max_freq = c;
                max_val = v;
            }
        }
        let mut need = max_freq * 2 - same;
        if need <= 0 {
            return ans;
        }
        for i in 0..n {
            if need <= 0 {
                break;
            }
            if nums1[i] != nums2[i] && nums1[i] != max_val && nums2[i] != max_val {
                ans += i as i64;
                need -= 1;
            }
        }
        if need > 0 {
            -1
        } else {
            ans
        }
    }
}

fn main() {}
