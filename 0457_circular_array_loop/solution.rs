// LeetCode 0457 - Circular Array Loop
// https://leetcode.com/problems/circular-array-loop/

impl Solution {
    pub fn circular_array_loop(nums: &mut Vec<i32>) -> bool {
        let length = nums.len() as i32;

        let next_index = |index: i32| -> i32 {
            let step = nums[index as usize];
            (index + step).rem_euclid(length)
        };

        for start in 0..length {
            if nums[start as usize] == 0 {
                continue;
            }

            let direction = if nums[start as usize] > 0 { 1 } else { -1 };
            let mut slow = start;
            let mut fast = start;

            loop {
                slow = next_index(slow);
                fast = next_index(next_index(fast));

                if nums[slow as usize] * direction <= 0
                    || nums[fast as usize] * direction <= 0
                    || nums[next_index(fast) as usize] * direction <= 0
                {
                    break;
                }
                if slow == fast {
                    if slow == next_index(slow) {
                        break;
                    }
                    return true;
                }
            }

            let mut index = start;
            let value = nums[start as usize];
            while nums[index as usize] * value > 0 {
                nums[index as usize] = 0;
                index = next_index(index);
            }
        }

        false
    }
}
