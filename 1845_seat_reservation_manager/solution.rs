// LeetCode 1845 - Seat Reservation Manager
// https://leetcode.com/problems/seat-reservation-manager/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

pub struct SeatManager {
    available: BinaryHeap<Reverse<i32>>,
}

impl SeatManager {
    pub fn new(n: i32) -> Self {
        let mut available = BinaryHeap::new();
        for seat in 1..=n {
            available.push(Reverse(seat));
        }
        Self { available }
    }

    pub fn reserve(&mut self) -> i32 {
        self.available.pop().unwrap().0
    }

    pub fn unreserve(&mut self, seat_number: i32) {
        self.available.push(Reverse(seat_number));
    }
}
