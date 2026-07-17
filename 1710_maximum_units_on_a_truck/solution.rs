// LeetCode 1710 - Maximum Units on a Truck
// https://leetcode.com/problems/maximum-units-on-a-truck/

impl Solution {
    pub fn maximum_units(box_types: Vec<Vec<i32>>, truck_size: i32) -> i32 {
        let mut box_types = box_types;
        let mut truck_size = truck_size;
        box_types.sort_unstable_by(|a, b| b[1].cmp(&a[1]));
        let mut total = 0;
        for item in &box_types {
            let take = item[0].min(truck_size);
            total += take * item[1];
            truck_size -= take;
            if truck_size == 0 {
                break;
            }
        }
        total
    }
}
