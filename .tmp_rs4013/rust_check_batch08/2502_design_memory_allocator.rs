// LeetCode 2502 - Design Memory Allocator
// https://leetcode.com/problems/design-memory-allocator/

pub struct Allocator {
    mem: Vec<i32>,
}

impl Allocator {
    pub fn new(n: i32) -> Self {
        Self {
            mem: vec![0; n as usize],
        }
    }

    pub fn allocate(&mut self, size: i32, m_id: i32) -> i32 {
        let mut free_cnt = 0;
        for i in 0..self.mem.len() {
            if self.mem[i] == 0 {
                free_cnt += 1;
                if free_cnt == size {
                    let start = i as i32 - size + 1;
                    for j in start as usize..=i {
                        self.mem[j] = m_id;
                    }
                    return start;
                }
            } else {
                free_cnt = 0;
            }
        }
        -1
    }

    pub fn free_memory(&mut self, m_id: i32) -> i32 {
        let mut cnt = 0;
        for x in &mut self.mem {
            if *x == m_id {
                *x = 0;
                cnt += 1;
            }
        }
        cnt
    }
}

fn main() {}
