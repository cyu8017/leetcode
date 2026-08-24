// LeetCode 0729 - My Calendar I
// https://leetcode.com/problems/my-calendar-i/

pub struct MyCalendar {
    bookings: Vec<(i32, i32)>,
}

impl MyCalendar {
    pub fn new() -> Self {
        Self {
            bookings: Vec::new(),
        }
    }

    pub fn book(&mut self, start_time: i32, end_time: i32) -> bool {
        for &(start, end) in &self.bookings {
            if start < end_time && start_time < end {
                return false;
            }
        }
        self.bookings.push((start_time, end_time));
        true
    }
}
