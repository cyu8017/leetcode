// LeetCode 2122 - Recover the Original Array
// https://leetcode.com/problems/recover-the-original-array/

impl Solution {
    pub fn recover_array(mut nums: Vec<i32>) -> Vec<i32> {
        nums.sort_unstable();
        let n = nums.len();
        for i in 1..n {
            let diff = nums[i] - nums[0];
            if diff == 0 || diff % 2 != 0 {
                continue;
            }
            let k = diff / 2;
            let mut used = vec![false; n];
            used[0] = true;
            used[i] = true;
            let mut ans = vec![(nums[0] + nums[i]) / 2];
            let mut l = 0;
            let mut r = i;
            let mut ok = true;
            while ans.len() < n / 2 {
                while l < n && used[l] {
                    l += 1;
                }
                if l == n {
                    ok = false;
                    break;
                }
                let need = nums[l] + 2 * k;
                while r < n && (used[r] || nums[r] < need) {
                    r += 1;
                }
                if r == n || nums[r] != need {
                    ok = false;
                    break;
                }
                used[l] = true;
                used[r] = true;
                ans.push(nums[l] + k);
            }
            if ok {
                return ans;
            }
        }
        vec![]
    }
}
