// LeetCode 1184 - Distance Between Bus Stops
// https://leetcode.com/problems/distance-between-bus-stops/

impl Solution {
    pub fn distance_between_bus_stops(distance: Vec<i32>, start: i32, destination: i32) -> i32 {
        let (mut start, mut destination) = (start as usize, destination as usize);
        if start > destination {
            std::mem::swap(&mut start, &mut destination);
        }
        let total: i32 = distance.iter().sum();
        let clockwise: i32 = distance[start..destination].iter().sum();
        clockwise.min(total - clockwise)
    }
}
