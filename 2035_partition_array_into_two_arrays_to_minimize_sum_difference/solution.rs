// LeetCode 2035 - Partition Array Into Two Arrays to Minimize Sum Difference
// https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/

impl Solution {
    pub fn minimum_difference(nums: Vec<i32>) -> i32 {
        let n = nums.len() / 2;
        let total: i32 = nums.iter().sum();
        fn sums_by_count(arr: &[i32]) -> Vec<Vec<i32>> {
            let m = arr.len();
            let mut res = vec![Vec::new(); m + 1];
            for mask in 0..(1 << m) {
                let mut sum = 0;
                let mut c = 0;
                for i in 0..m {
                    if mask & (1 << i) != 0 {
                        sum += arr[i];
                        c += 1;
                    }
                }
                res[c].push(sum);
            }
            for v in &mut res {
                v.sort_unstable();
            }
            res
        }
        let left = &nums[..n];
        let right = &nums[n..];
        let l = sums_by_count(left);
        let r = sums_by_count(right);
        let mut ans = i32::MAX;
        for k in 0..=n {
            for &s1 in &l[k] {
                let need = total / 2 - s1;
                let arr = &r[n - k];
                let idx = arr.partition_point(|&x| x < need);
                for i in [idx as i32 - 1, idx as i32] {
                    if i >= 0 && (i as usize) < arr.len() {
                        let s2 = arr[i as usize];
                        ans = ans.min((total - 2 * (s1 + s2)).abs());
                    }
                }
            }
        }
        ans
    }
}
