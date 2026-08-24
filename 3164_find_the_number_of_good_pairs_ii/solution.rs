// LeetCode 3164 - Find the Number of Good Pairs II
// https://leetcode.com/problems/find-the-number-of-good-pairs-ii/

use std::collections::HashMap;

impl Solution {
    pub fn number_of_pairs(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i64 {
        let mut cnt1: HashMap<i32, i32> = HashMap::new();
        for x in nums1 {
            if x % k == 0 {
                *cnt1.entry(x / k).or_insert(0) += 1;
            }
        }
        if cnt1.is_empty() {
            return 0;
        }
        let mut cnt2: HashMap<i32, i32> = HashMap::new();
        for x in nums2 {
            *cnt2.entry(x).or_insert(0) += 1;
        }
        let mx = *cnt1.keys().max().unwrap();
        let mut ans = 0i64;
        for (&x, &v) in &cnt2 {
            let mut s = 0i32;
            let mut y = x;
            while y <= mx {
                if let Some(&c) = cnt1.get(&y) {
                    s += c;
                }
                y += x;
            }
            ans += s as i64 * v as i64;
        }
        ans
    }
}
