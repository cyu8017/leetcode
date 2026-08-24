// LeetCode 2040 - Kth Smallest Product of Two Sorted Arrays
// https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

impl Solution {
    pub fn kth_smallest_product(nums1: Vec<i32>, nums2: Vec<i32>, k: i64) -> i64 {
        let count_le = |x: i64| -> i64 {
            let mut cnt = 0i64;
            for &a in &nums1 {
                if a > 0 {
                    let mut lo = 0;
                    let mut hi = nums2.len();
                    while lo < hi {
                        let mid = (lo + hi) / 2;
                        if a as i64 * nums2[mid] as i64 <= x {
                            lo = mid + 1;
                        } else {
                            hi = mid;
                        }
                    }
                    cnt += lo as i64;
                } else if a < 0 {
                    let mut lo = 0;
                    let mut hi = nums2.len();
                    while lo < hi {
                        let mid = (lo + hi) / 2;
                        if a as i64 * nums2[mid] as i64 <= x {
                            hi = mid;
                        } else {
                            lo = mid + 1;
                        }
                    }
                    cnt += (nums2.len() - lo) as i64;
                } else if x >= 0 {
                    cnt += nums2.len() as i64;
                }
            }
            cnt
        };
        let mut lo = -10_000_000_000i64;
        let mut hi = 10_000_000_000i64;
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if count_le(mid) >= k {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
