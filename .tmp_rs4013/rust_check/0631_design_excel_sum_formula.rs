// LeetCode 0631 - Design Excel Sum Formula
// https://leetcode.com/problems/design-excel-sum-formula/

use std::collections::HashMap;

pub struct Excel {
    values: Vec<Vec<i32>>,
    formulas: HashMap<(i32, usize), Vec<(i32, usize)>>,
}

impl Excel {
    pub fn new(height: i32, width: char) -> Self {
        let width = (width as u8 - b'A' + 1) as usize;
        Self {
            values: vec![vec![0; width]; (height + 1) as usize],
            formulas: HashMap::new(),
        }
    }

    fn parse(cell: &str) -> (i32, usize) {
        let col = (cell.as_bytes()[0] - b'A') as usize;
        let row: i32 = cell[1..].parse().unwrap();
        (row, col)
    }

    fn eval(&self, row: i32, col: usize) -> i32 {
        if let Some(cells) = self.formulas.get(&(row, col)) {
            return cells.iter().map(|&(r, c)| self.eval(r, c)).sum();
        }
        self.values[row as usize][col]
    }

    pub fn set(&mut self, row: i32, column: char, val: i32) {
        let col = (column as u8 - b'A') as usize;
        self.formulas.remove(&(row, col));
        self.values[row as usize][col] = val;
    }

    pub fn get(&self, row: i32, column: char) -> i32 {
        self.eval(row, (column as u8 - b'A') as usize)
    }

    pub fn sum(&mut self, row: i32, column: char, numbers: Vec<String>) -> i32 {
        let col = (column as u8 - b'A') as usize;
        let mut cells = Vec::new();
        for token in numbers {
            if let Some(pos) = token.find(':') {
                let (r1, c1) = Self::parse(&token[..pos]);
                let (r2, c2) = Self::parse(&token[pos + 1..]);
                for r in r1..=r2 {
                    for c in c1..=c2 {
                        cells.push((r, c));
                    }
                }
            } else {
                cells.push(Self::parse(&token));
            }
        }
        self.formulas.insert((row, col), cells);
        self.eval(row, col)
    }
}

fn main() {}
