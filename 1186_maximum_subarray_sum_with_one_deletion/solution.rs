// LeetCode 1186 - Maximum Subarray Sum with One Deletion
// https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

impl Solution {
    pub fn maximum_sum(arr: Vec<i32>) -> i32 {
        let mut keep = arr[0];
        let mut delete = arr[0];
        let mut ans = arr[0];
        for &x in &arr[1..] {
            let nd = keep.max(delete + x);
            let nk = (keep + x).max(x);
            keep = nk;
            delete = nd;
            ans = ans.max(keep).max(delete);
        }
        ans
    }
}
