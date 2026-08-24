fn main() {}

// LeetCode 2726 - Calculator with Method Chaining
// https://leetcode.com/problems/calculator-with-method-chaining/

pub struct Calculator {
    val: f64,
}

impl Calculator {
    pub fn new(value: f64) -> Self {
        Self { val: value }
    }

    pub fn add(&mut self, value: f64) -> &mut Self {
        self.val += value;
        self
    }

    pub fn subtract(&mut self, value: f64) -> &mut Self {
        self.val -= value;
        self
    }

    pub fn multiply(&mut self, value: f64) -> &mut Self {
        self.val *= value;
        self
    }

    pub fn divide(&mut self, value: f64) -> &mut Self {
        if value != 0.0 {
            self.val /= value;
        }
        self
    }

    pub fn power(&mut self, value: f64) -> &mut Self {
        self.val = self.val.powf(value);
        self
    }

    pub fn get_result(&self) -> f64 {
        self.val
    }
}
