// LeetCode 0731 - My Calendar II
// https://leetcode.com/problems/my-calendar-ii/

pub struct MyCalendarTwo {
    booked: Vec<(i32, i32)>,
    overlaps: Vec<(i32, i32)>,
}

impl MyCalendarTwo {
    pub fn new() -> Self {
        Self {
            booked: Vec::new(),
            overlaps: Vec::new(),
        }
    }

    pub fn book(&mut self, start_time: i32, end_time: i32) -> bool {
        for &(start, end) in &self.overlaps {
            if start < end_time && start_time < end {
                return false;
            }
        }
        for &(start, end) in &self.booked {
            if start < end_time && start_time < end {
                self.overlaps
                    .push((start.max(start_time), end.min(end_time)));
            }
        }
        self.booked.push((start_time, end_time));
        true
    }
}
