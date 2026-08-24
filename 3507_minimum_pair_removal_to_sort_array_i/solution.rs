// LeetCode 3507 - Minimum Pair Removal to Sort Array I
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

impl Solution {
    fn is_non_decreasing(a: &[i32]) -> bool {
        for i in 1..a.len() {
            if a[i] < a[i - 1] {
                return false;
            }
        }
        true
    }

    pub fn minimum_pair_removal(nums: Vec<i32>) -> i32 {
        let mut arr = nums;
        let mut ans = 0;
        while !Self::is_non_decreasing(&arr) {
            let mut k = 0;
            let mut s = arr[0] + arr[1];
            for i in 1..arr.len() - 1 {
                let t = arr[i] + arr[i + 1];
                if s > t {
                    s = t;
                    k = i;
                }
            }
            arr[k] = s;
            arr.remove(k + 1);
            ans += 1;
        }
        ans
    }
}
