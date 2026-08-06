// LeetCode 1472 - Design Browser History
// https://leetcode.com/problems/design-browser-history/

struct BrowserHistory {
    history: Vec<String>,
    index: usize,
}

impl BrowserHistory {
    fn new(homepage: String) -> Self {
        Self {
            history: vec![homepage],
            index: 0,
        }
    }

    fn visit(&mut self, url: String) {
        self.history.truncate(self.index + 1);
        self.history.push(url);
        self.index += 1;
    }

    fn back(&mut self, steps: i32) -> String {
        self.index = self.index.saturating_sub(steps as usize);
        self.history[self.index].clone()
    }

    fn forward(&mut self, steps: i32) -> String {
        self.index = (self.index + steps as usize).min(self.history.len() - 1);
        self.history[self.index].clone()
    }
}
