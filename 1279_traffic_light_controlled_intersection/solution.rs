// LeetCode 1279 - Traffic Light Controlled Intersection
// https://leetcode.com/problems/traffic-light-controlled-intersection/

use std::sync::Mutex;

struct TrafficLight {
    green_road: Mutex<i32>,
}

impl TrafficLight {
    fn new() -> Self {
        Self {
            green_road: Mutex::new(1),
        }
    }

    fn car_arrived(
        &self,
        _car_id: i32,
        road_id: i32,
        _direction: i32,
        turn_green: impl FnOnce(),
        cross_car: impl FnOnce(),
    ) {
        let mut green = self.green_road.lock().unwrap();
        if road_id != *green {
            turn_green();
            *green = road_id;
        }
        cross_car();
    }
}
