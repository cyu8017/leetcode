// LeetCode 1396 - Design Underground System
// https://leetcode.com/problems/design-underground-system/

use std::collections::HashMap;

struct UndergroundSystem {
    ins: HashMap<i32, (String, i32)>,
    stats: HashMap<(String, String), (i32, i32)>,
}

impl UndergroundSystem {
    fn new() -> Self {
        Self {
            ins: HashMap::new(),
            stats: HashMap::new(),
        }
    }

    fn check_in(&mut self, id: i32, station_name: String, t: i32) {
        self.ins.insert(id, (station_name, t));
    }

    fn check_out(&mut self, id: i32, station_name: String, t: i32) {
        let (start, begin) = self.ins.remove(&id).unwrap();
        let entry = self.stats.entry((start, station_name)).or_insert((0, 0));
        entry.0 += t - begin;
        entry.1 += 1;
    }

    fn get_average_time(&self, start_station: String, end_station: String) -> f64 {
        let (total, count) = self.stats[&(start_station, end_station)];
        total as f64 / count as f64
    }
}
