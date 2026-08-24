// LeetCode 3134 - Find the Median of the Uniqueness Array
// https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/

use std::collections::HashMap;

impl Solution {
    pub fn median_of_uniqueness_array(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let m = (1 + n as i64) * n as i64 / 2;
        let check = |mx: usize| -> bool {
            let mut cnt: HashMap<i32, i32> = HashMap::new();
            let mut l = 0usize;
            let mut k = 0i64;
            for r in 0..n {
                *cnt.entry(nums[r]).or_insert(0) += 1;
                while cnt.len() > mx {
                    let y = nums[l];
                    l += 1;
                    let e = cnt.get_mut(&y).unwrap();
                    *e -= 1;
                    if *e == 0 {
                        cnt.remove(&y);
                    }
                }
                k += (r - l + 1) as i64;
                if k >= (m + 1) / 2 {
                    return true;
                }
            }
            false
        };
        let mut lo = 1usize;
        let mut hi = n;
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if check(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo as i32
    }
}
