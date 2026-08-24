// LeetCode 3041 - Maximize Consecutive Elements in an Array After Modification
// https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/

use std::collections::HashMap;

impl Solution {
    pub fn max_selected_elements(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let mut dp: HashMap<i32, i32> = HashMap::new();
        let mut ans = 0;
        for num in nums {
            let v_num = *dp.get(&num).unwrap_or(&0);
            let v_prev = *dp.get(&(num - 1)).unwrap_or(&0);
            dp.insert(num + 1, v_num + 1);
            dp.insert(num, v_prev + 1);
            ans = ans.max(*dp.get(&num).unwrap()).max(*dp.get(&(num + 1)).unwrap());
        }
        ans
    }
}
