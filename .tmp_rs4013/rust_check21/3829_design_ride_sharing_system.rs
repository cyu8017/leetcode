// LeetCode 3829 - Design Ride Sharing System
// https://leetcode.com/problems/design-ride-sharing-system/

use std::collections::{BTreeMap, HashMap};

pub struct RideSharingSystem {
    t: i32,
    riders: BTreeMap<i32, i32>,
    drivers: BTreeMap<i32, i32>,
    d: HashMap<i32, i32>,
}

impl RideSharingSystem {
    pub fn new() -> Self {
        Self {
            t: 0,
            riders: BTreeMap::new(),
            drivers: BTreeMap::new(),
            d: HashMap::new(),
        }
    }

    pub fn add_rider(&mut self, rider_id: i32) {
        self.d.insert(rider_id, self.t);
        self.riders.insert(self.t, rider_id);
        self.t += 1;
    }

    pub fn add_driver(&mut self, driver_id: i32) {
        self.drivers.insert(self.t, driver_id);
        self.t += 1;
    }

    pub fn match_driver_with_rider(&mut self) -> Vec<i32> {
        if self.riders.is_empty() || self.drivers.is_empty() {
            return vec![-1, -1];
        }
        let (&dt, &driver_id) = self.drivers.iter().next().unwrap();
        let (&rt, &rider_id) = self.riders.iter().next().unwrap();
        self.drivers.remove(&dt);
        self.riders.remove(&rt);
        vec![driver_id, rider_id]
    }

    pub fn cancel_rider(&mut self, rider_id: i32) {
        if let Some(t) = self.d.get(&rider_id) {
            self.riders.remove(t);
        }
    }
}
