// LeetCode 0815 - Bus Routes
// https://leetcode.com/problems/bus-routes/

use std::collections::{HashMap, HashSet, VecDeque};

impl Solution {
    pub fn num_buses_to_destination(routes: Vec<Vec<i32>>, source: i32, target: i32) -> i32 {
        if source == target {
            return 0;
        }
        let mut stop_to_buses: HashMap<i32, Vec<usize>> = HashMap::new();
        for (bus, stops) in routes.iter().enumerate() {
            for &stop in stops {
                stop_to_buses.entry(stop).or_default().push(bus);
            }
        }
        let mut queue = VecDeque::new();
        queue.push_back((source, 0));
        let mut seen_stops = HashSet::from([source]);
        let mut seen_buses = HashSet::new();
        while let Some((stop, buses_taken)) = queue.pop_front() {
            if let Some(buses) = stop_to_buses.get(&stop) {
                for &bus in buses {
                    if !seen_buses.insert(bus) {
                        continue;
                    }
                    for &nxt in &routes[bus] {
                        if nxt == target {
                            return buses_taken + 1;
                        }
                        if seen_stops.insert(nxt) {
                            queue.push_back((nxt, buses_taken + 1));
                        }
                    }
                }
            }
        }
        -1
    }
}
