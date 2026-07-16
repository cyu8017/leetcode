// LeetCode 0335 - Self Crossing
// https://leetcode.com/problems/self-crossing/

impl Solution {
    pub fn is_self_crossing(distance: Vec<i32>) -> bool {
        for index in 3..distance.len() {
            if distance[index] >= distance[index - 2]
                && distance[index - 1] <= distance[index - 3]
            {
                return true;
            }
            if index >= 4 && distance[index - 1] == distance[index - 3] {
                if distance[index - 2] >= distance[index - 4] + distance[index] {
                    return true;
                }
            }
            if index >= 5 {
                if distance[index - 4] >= distance[index - 2] - distance[index] {
                    if distance[index] >= distance[index - 2] - distance[index - 4] {
                        if distance[index - 1] <= distance[index - 3] {
                            if distance[index - 5] + distance[index - 1] >= distance[index - 3] {
                                return true;
                            }
                        }
                    }
                }
            }
        }
        false
    }
}
