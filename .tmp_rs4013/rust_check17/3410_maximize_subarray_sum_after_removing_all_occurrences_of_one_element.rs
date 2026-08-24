struct Solution;
// LeetCode 3410 - Maximize Subarray Sum After Removing All Occurrences of One Element
// https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/

use std::collections::HashSet;

impl Solution {
    fn kadane(a: &[i32]) -> i64 {
        let mut best = -(1i64 << 62);
        let mut cur = 0i64;
        for &x in a {
            cur += x as i64;
            if cur > best {
                best = cur;
            }
            if cur < 0 {
                cur = 0;
            }
        }
        let mut all_neg = true;
        let mut mx = a[0] as i64;
        for &x in a {
            if x as i64 > mx {
                mx = x as i64;
            }
            if x >= 0 {
                all_neg = false;
            }
        }
        if all_neg {
            mx
        } else {
            best
        }
    }

    pub fn max_subarray_sum(nums: Vec<i32>) -> i64 {
        let mut ans = Self::kadane(&nums);
        let mut uniq = HashSet::new();
        for &x in &nums {
            if x < 0 {
                uniq.insert(x);
            }
        }
        for v in uniq {
            let b: Vec<i32> = nums.iter().copied().filter(|&x| x != v).collect();
            if b.is_empty() {
                continue;
            }
            let cand = Self::kadane(&b);
            if cand > ans {
                ans = cand;
            }
        }
        ans
    }
}

fn main() {}
