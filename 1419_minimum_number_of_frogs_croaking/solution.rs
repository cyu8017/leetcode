// LeetCode 1419 - Minimum Number of Frogs Croaking
// https://leetcode.com/problems/minimum-number-of-frogs-croaking/

impl Solution {
    pub fn min_number_of_frogs(croak_of_frogs: String) -> i32 {
        let order = [b'c', b'r', b'o', b'a', b'k'];
        let mut counts = [0i32; 5];
        let mut active = 0;
        let mut answer = 0;
        for char in croak_of_frogs.bytes() {
            let i = match order.iter().position(|&c| c == char) {
                Some(i) => i,
                None => return -1,
            };
            if i > 0 && counts[i - 1] == 0 {
                return -1;
            }
            if i > 0 {
                counts[i - 1] -= 1;
            }
            counts[i] += 1;
            if i == 0 {
                active += 1;
                answer = answer.max(active);
            } else if i == 4 {
                counts[4] -= 1;
                active -= 1;
            }
        }
        if active == 0 { answer } else { -1 }
    }
}
