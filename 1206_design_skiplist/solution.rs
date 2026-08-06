// LeetCode 1206 - Design Skiplist
// https://leetcode.com/problems/design-skiplist/

struct Skiplist {
    values: Vec<i32>,
}

impl Skiplist {
    fn new() -> Self {
        Self { values: Vec::new() }
    }

    fn search(&self, target: i32) -> bool {
        self.values.binary_search(&target).is_ok()
    }

    fn add(&mut self, num: i32) {
        let i = self.values.partition_point(|&x| x < num);
        self.values.insert(i, num);
    }

    fn erase(&mut self, num: i32) -> bool {
        if let Ok(i) = self.values.binary_search(&num) {
            self.values.remove(i);
            true
        } else {
            false
        }
    }
}
