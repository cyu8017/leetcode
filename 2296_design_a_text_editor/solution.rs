// LeetCode 2296 - Design a Text Editor
// https://leetcode.com/problems/design-a-text-editor/

pub struct TextEditor {
    left: Vec<char>,
    right: Vec<char>,
}

impl TextEditor {
    pub fn new() -> Self {
        Self {
            left: Vec::new(),
            right: Vec::new(),
        }
    }

    fn suffix(&self) -> String {
        let start = self.left.len().saturating_sub(10);
        self.left[start..].iter().collect()
    }

    pub fn add_text(&mut self, text: String) {
        self.left.extend(text.chars());
    }

    pub fn delete_text(&mut self, mut k: i32) -> i32 {
        let mut deleted = 0;
        while k > 0 && !self.left.is_empty() {
            self.left.pop();
            k -= 1;
            deleted += 1;
        }
        deleted
    }

    pub fn cursor_left(&mut self, mut k: i32) -> String {
        while k > 0 && !self.left.is_empty() {
            let c = self.left.pop().unwrap();
            self.right.push(c);
            k -= 1;
        }
        self.suffix()
    }

    pub fn cursor_right(&mut self, mut k: i32) -> String {
        while k > 0 && !self.right.is_empty() {
            let c = self.right.pop().unwrap();
            self.left.push(c);
            k -= 1;
        }
        self.suffix()
    }
}
