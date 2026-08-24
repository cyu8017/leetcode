// LeetCode 3484 - Design Spreadsheet
// https://leetcode.com/problems/design-spreadsheet/

use std::collections::HashMap;

pub struct Spreadsheet {
    cells: HashMap<String, i32>,
}

impl Spreadsheet {
    pub fn new(_rows: i32) -> Self {
        Self {
            cells: HashMap::new(),
        }
    }

    pub fn set_cell(&mut self, cell: String, value: i32) {
        self.cells.insert(cell, value);
    }

    pub fn reset_cell(&mut self, cell: String) {
        self.cells.remove(&cell);
    }

    pub fn get_value(&self, formula: String) -> i32 {
        let formula = if formula.starts_with('=') {
            &formula[1..]
        } else {
            &formula
        };
        let mut sum = 0;
        let mut start = 0;
        let chars: Vec<char> = formula.chars().collect();
        while start < chars.len() {
            let plus = chars[start..].iter().position(|&c| c == '+');
            let end = plus.map(|p| start + p).unwrap_or(chars.len());
            let p: String = chars[start..end].iter().collect();
            let mut is_num = !p.is_empty()
                && (p.as_bytes()[0].is_ascii_digit()
                    || (p.as_bytes()[0] == b'-' && p.len() > 1));
            if is_num {
                for i in 1..p.len() {
                    if !p.as_bytes()[i].is_ascii_digit() {
                        is_num = false;
                        break;
                    }
                }
            }
            if is_num {
                sum += p.parse::<i32>().unwrap_or(0);
            } else {
                sum += self.cells.get(&p).copied().unwrap_or(0);
            }
            if plus.is_none() {
                break;
            }
            start = end + 1;
        }
        sum
    }
}

fn main() {}
