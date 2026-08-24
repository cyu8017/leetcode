// LeetCode 3132 - Find the Integer Added to Array II
// https://leetcode.com/problems/find-the-integer-added-to-array-ii/

impl Solution {
    pub fn minimum_added_integer(mut nums1: Vec<i32>, mut nums2: Vec<i32>) -> i32 {
        nums1.sort_unstable();
        nums2.sort_unstable();
        let mut ans = 1 << 30;
        let f = |x: i32| -> bool {
            let mut i = 0usize;
            let mut j = 0usize;
            let mut cnt = 0;
            while i < nums1.len() && j < nums2.len() {
                if nums2[j] - nums1[i] != x {
                    cnt += 1;
                } else {
                    j += 1;
                }
                i += 1;
            }
            cnt <= 2
        };
        for t in 0..3 {
            let x = nums2[0] - nums1[t];
            if f(x) {
                ans = ans.min(x);
            }
        }
        ans
    }
}
