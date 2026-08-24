struct Solution;
fn main() {}

// LeetCode 2728 - Count Houses in a Circular Street
// https://leetcode.com/problems/count-houses-in-a-circular-street/

pub trait Street {
    fn open_door(&mut self);
    fn close_door(&mut self);
    fn is_door_open(&self) -> bool;
    fn move_right(&mut self);
    fn move_left(&mut self);
}

impl Solution {
    pub fn count_houses<S: Street>(street: &mut S, k: i32) -> i32 {
        for _ in 0..k {
            street.close_door();
            street.move_right();
        }
        let mut ans = 0;
        loop {
            ans += 1;
            street.open_door();
            street.move_right();
            if street.is_door_open() {
                break;
            }
        }
        ans
    }
}
