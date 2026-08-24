// LeetCode 3659 - Partition Array Into K-Distinct Groups
// https://leetcode.com/problems/partition-array-into-k-distinct-groups/

impl Solution {
    pub fn partition_array(nums: Vec<i32>, k: i32) -> bool {
        let n = nums.len();
        if n as i32 % k != 0 {
            return false;
        }
        let m = n as i32 / k;
        let mx = *nums.iter().max().unwrap();
        let mut cnt = vec![0; (mx + 1) as usize];
        for x in nums {
            cnt[x as usize] += 1;
            if cnt[x as usize] > m {
                return false;
            }
        }
        true
    }
}
