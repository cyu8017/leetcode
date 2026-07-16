// LeetCode 0277 - Find the Celebrity
// https://leetcode.com/problems/find-the-celebrity/

fn knows(a: i32, b: i32) -> bool {
    let _ = (a, b);
    false
}

impl Solution {
    pub fn find_celebrity(n: i32) -> i32 {
        let mut candidate = 0;
        for person in 1..n {
            if knows(candidate, person) {
                candidate = person;
            }
        }
        for person in 0..n {
            if person == candidate {
                continue;
            }
            if knows(candidate, person) || !knows(person, candidate) {
                return -1;
            }
        }
        candidate
    }
}
