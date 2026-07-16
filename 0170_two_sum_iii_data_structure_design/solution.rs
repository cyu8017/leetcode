// LeetCode 0170 - Two Sum III - Data structure design
use std::collections::HashMap;
struct TwoSum {
    counts: HashMap<i32, i32>,
}
impl TwoSum {
    fn new() -> Self { Self { counts: HashMap::new() } }
    fn add(&mut self, number: i32) { *self.counts.entry(number).or_insert(0) += 1; }
    fn find(&self, value: i32) -> bool {
        self.counts.iter().any(|(&number, &count)| {
            let complement = value - number;
            if complement == number { count >= 2 } else { self.counts.contains_key(&complement) }
        })
    }
}