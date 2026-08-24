// LeetCode 3508 - Implement Router
// https://leetcode.com/problems/implement-router/

use std::collections::{HashMap, HashSet, VecDeque};

pub struct Router {
    lim: usize,
    vis: HashSet<i64>,
    q: VecDeque<[i32; 3]>,
    idx: HashMap<i32, usize>,
    d: HashMap<i32, Vec<i32>>,
}

impl Router {
    fn f(a: i32, b: i32, c: i32) -> i64 {
        ((a as i64) << 46) | ((b as i64) << 29) | (c as i64)
    }

    pub fn new(memory_limit: i32) -> Self {
        Self {
            lim: memory_limit as usize,
            vis: HashSet::new(),
            q: VecDeque::new(),
            idx: HashMap::new(),
            d: HashMap::new(),
        }
    }

    pub fn add_packet(&mut self, source: i32, destination: i32, timestamp: i32) -> bool {
        let x = Self::f(source, destination, timestamp);
        if self.vis.contains(&x) {
            return false;
        }
        self.vis.insert(x);
        if self.q.len() >= self.lim {
            self.forward_packet();
        }
        self.q.push_back([source, destination, timestamp]);
        self.d.entry(destination).or_default().push(timestamp);
        true
    }

    pub fn forward_packet(&mut self) -> Vec<i32> {
        if self.q.is_empty() {
            return vec![];
        }
        let packet = self.q.pop_front().unwrap();
        let (s, dest, t) = (packet[0], packet[1], packet[2]);
        self.vis.remove(&Self::f(s, dest, t));
        *self.idx.entry(dest).or_insert(0) += 1;
        vec![s, dest, t]
    }

    pub fn get_count(&self, destination: i32, start_time: i32, end_time: i32) -> i32 {
        let ls = match self.d.get(&destination) {
            Some(v) => v,
            None => return 0,
        };
        let k = *self.idx.get(&destination).unwrap_or(&0);
        let tail = &ls[k.min(ls.len())..];
        let it1 = tail.partition_point(|&x| x < start_time);
        let it2 = tail.partition_point(|&x| x < end_time + 1);
        (it2 - it1) as i32
    }
}
