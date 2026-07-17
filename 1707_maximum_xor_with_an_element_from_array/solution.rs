// LeetCode 1707 - Maximum XOR With an Element From Array
// https://leetcode.com/problems/maximum-xor-with-an-element-from-array/

impl Solution {
    pub fn maximize_xor(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut nums = nums;
        nums.sort_unstable();
        let mut order: Vec<usize> = (0..queries.len()).collect();
        order.sort_unstable_by_key(|&i| queries[i][1]);

        let mut children: Vec<[i32; 2]> = vec![[-1, -1]];
        let mut ans = vec![-1; queries.len()];
        let mut added = 0usize;

        for &qi in &order {
            let x = queries[qi][0];
            let limit = queries[qi][1];
            while added < nums.len() && nums[added] <= limit {
                let num = nums[added];
                let mut node = 0usize;
                for bit in (0..32).rev() {
                    let b = ((num >> bit) & 1) as usize;
                    if children[node][b] == -1 {
                        children[node][b] = children.len() as i32;
                        children.push([-1, -1]);
                    }
                    node = children[node][b] as usize;
                }
                added += 1;
            }
            if added == 0 {
                continue;
            }
            let mut node = 0usize;
            let mut value = 0i32;
            for bit in (0..32).rev() {
                let b = ((x >> bit) & 1) as usize;
                let want = b ^ 1;
                if children[node][want] != -1 {
                    value |= 1 << bit;
                    node = children[node][want] as usize;
                } else {
                    node = children[node][b] as usize;
                }
            }
            ans[qi] = value;
        }
        ans
    }
}
