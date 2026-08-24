// LeetCode 3948 - Lexicographically Maximum MEX Array
// https://leetcode.com/problems/lexicographically-maximum-mex-array/

impl Solution {
    pub fn max_mex_array(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut remaining = vec![0; n + 2];
        for &x in &nums {
            if x <= n as i32 + 1 {
                remaining[x as usize] += 1;
            }
        }
        let mut mex = 0;
        while remaining[mex] > 0 {
            mex += 1;
        }
        let mut answer = Vec::new();
        let mut seen = vec![0; n + 2];
        let mut stamp = 0;
        let mut index = 0;
        while index < n {
            if mex == 0 {
                answer.push(0);
                let x = nums[index];
                if x <= n as i32 + 1 {
                    remaining[x as usize] -= 1;
                }
                index += 1;
                continue;
            }
            stamp += 1;
            let mut need = mex;
            while need > 0 {
                let x = nums[index];
                if x < mex as i32 && seen[x as usize] != stamp {
                    seen[x as usize] = stamp;
                    need -= 1;
                }
                if x <= n as i32 + 1 {
                    remaining[x as usize] -= 1;
                }
                index += 1;
            }
            answer.push(mex as i32);
            mex = 0;
            while remaining[mex] > 0 {
                mex += 1;
            }
        }
        answer
    }
}
