// LeetCode 2069 - Walking Robot Simulation II
// https://leetcode.com/problems/walking-robot-simulation-ii/

pub struct Robot {
    w: i32,
    h: i32,
    peri: i32,
    pos: i32,
    moved: bool,
}

impl Robot {
    pub fn new(width: i32, height: i32) -> Self {
        Self {
            w: width,
            h: height,
            peri: 2 * (width + height) - 4,
            pos: 0,
            moved: false,
        }
    }

    fn pos_dir(&self) -> (i32, i32, String) {
        let mut p = self.pos;
        if p == 0 {
            if !self.moved {
                return (0, 0, "East".to_string());
            }
            return (0, 0, "South".to_string());
        }
        if p <= self.w - 1 {
            return (p, 0, "East".to_string());
        }
        p -= self.w - 1;
        if p <= self.h - 1 {
            return (self.w - 1, p, "North".to_string());
        }
        p -= self.h - 1;
        if p <= self.w - 1 {
            return (self.w - 1 - p, self.h - 1, "West".to_string());
        }
        p -= self.w - 1;
        (0, self.h - 1 - p, "South".to_string())
    }

    pub fn step(&mut self, num: i32) {
        self.moved = true;
        self.pos = (self.pos + num) % self.peri;
    }

    pub fn get_pos(&self) -> Vec<i32> {
        let (x, y, _) = self.pos_dir();
        vec![x, y]
    }

    pub fn get_dir(&self) -> String {
        self.pos_dir().2
    }
}
