// LeetCode 0352 - Data Stream as Disjoint Intervals
// https://leetcode.com/problems/data-stream-as-disjoint-intervals/

struct SummaryRanges {
    intervals: Vec<Vec<i32>>,
}

impl SummaryRanges {
    fn new() -> Self {
        Self {
            intervals: Vec::new(),
        }
    }

    fn add_num(&mut self, value: i32) {
        let mut new_interval = vec![value, value];
        let mut merged = Vec::new();
        let mut inserted = false;

        for interval in &self.intervals {
            if interval[1] < value - 1 {
                merged.push(interval.clone());
            } else if interval[0] > value + 1 {
                if !inserted {
                    merged.push(new_interval.clone());
                    inserted = true;
                }
                merged.push(interval.clone());
            } else {
                new_interval[0] = new_interval[0].min(interval[0]);
                new_interval[1] = new_interval[1].max(interval[1]);
            }
        }

        if !inserted {
            merged.push(new_interval);
        }

        self.intervals = merged;
    }

    fn get_intervals(&self) -> Vec<Vec<i32>> {
        self.intervals.clone()
    }
}
