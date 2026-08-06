// LeetCode 1146 - Snapshot Array
// https://leetcode.com/problems/snapshot-array/

struct SnapshotArray {
    snap_id: i32,
    data: Vec<Vec<(i32, i32)>>,
}

impl SnapshotArray {
    fn new(length: i32) -> Self {
        Self {
            snap_id: 0,
            data: vec![vec![(0, 0)]; length as usize],
        }
    }

    fn set(&mut self, index: i32, val: i32) {
        let hist = &mut self.data[index as usize];
        if hist.last().unwrap().0 == self.snap_id {
            hist.last_mut().unwrap().1 = val;
        } else {
            hist.push((self.snap_id, val));
        }
    }

    fn snap(&mut self) -> i32 {
        let id = self.snap_id;
        self.snap_id += 1;
        id
    }

    fn get(&self, index: i32, snap_id: i32) -> i32 {
        let hist = &self.data[index as usize];
        let i = hist.partition_point(|&(sid, _)| sid <= snap_id);
        hist[i - 1].1
    }
}
