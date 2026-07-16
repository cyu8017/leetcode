// LeetCode 0416 - Partition Equal Subset Sum
// https://leetcode.com/problems/partition-equal-subset-sum/

use std::collections::HashSet;

impl Solution {
    pub fn can_partition(nums: Vec<i32>) -> bool {
        let total: i32 = nums.iter().sum();
        if total % 2 != 0 {
            return false;
        }

        let target = total / 2;
        let mut possible = HashSet::from([0]);

        for value in nums {
            let next: HashSet<i32> = possible
                .iter()
                .flat_map(|amount| {
                    let mut items = vec![*amount];
                    if amount + value <= target {
                        items.push(amount + value);
                    }
                    items
                })
                .collect();
            possible = next;
            if possible.contains(&target) {
                return true;
            }
        }

        possible.contains(&target)
    }
}
