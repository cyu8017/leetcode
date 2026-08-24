// LeetCode 0881 - Boats to Save People
// https://leetcode.com/problems/boats-to-save-people/

impl Solution {
    pub fn num_rescue_boats(mut people: Vec<i32>, limit: i32) -> i32 {
        people.sort_unstable();
        let mut i = 0i32;
        let mut j = people.len() as i32 - 1;
        let mut boats = 0;
        while i <= j {
            if people[i as usize] + people[j as usize] <= limit {
                i += 1;
            }
            j -= 1;
            boats += 1;
        }
        boats
    }
}
