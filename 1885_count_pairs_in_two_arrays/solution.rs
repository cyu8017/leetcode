// LeetCode 1885 - Count Pairs in Two Arrays
// https://leetcode.com/problems/count-pairs-in-two-arrays/

impl Solution {
    pub fn count_pairs(nums1: Vec<i32>, nums2: Vec<i32>) -> i64 {
        let mut diff: Vec<i32> = nums1
            .iter()
            .zip(nums2.iter())
            .map(|(a, b)| a - b)
            .collect();
        diff.sort_unstable();
        let mut answer = 0i64;
        let n = diff.len();
        for i in 0..n {
            let target = -diff[i];
            let mut lo = i + 1;
            let mut hi = n;
            while lo < hi {
                let mid = (lo + hi) / 2;
                if diff[mid] > target {
                    hi = mid;
                } else {
                    lo = mid + 1;
                }
            }
            answer += (n - lo) as i64;
        }
        answer
    }
}
