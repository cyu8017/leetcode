// LeetCode 1603 - Design Parking System
// https://leetcode.com/problems/design-parking-system/

pub struct ParkingSystem {
    spaces: [i32; 4],
}

impl ParkingSystem {
    pub fn new(big: i32, medium: i32, small: i32) -> Self {
        Self { spaces: [0, big, medium, small] }
    }

    pub fn add_car(&mut self, car_type: i32) -> bool {
        let idx = car_type as usize;
        if self.spaces[idx] == 0 {
            return false;
        }
        self.spaces[idx] -= 1;
        true
    }
}
