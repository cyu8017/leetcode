// LeetCode 0341 - Flatten Nested List Iterator
// https://leetcode.com/problems/flatten-nested-list-iterator/

pub struct NestedInteger {
    integer: Option<i32>,
    list: Vec<NestedInteger>,
}

impl NestedInteger {
    pub fn new(value: Option<i32>) -> Self {
        NestedInteger {
            integer: value,
            list: Vec::new(),
        }
    }

    pub fn is_integer(&self) -> bool {
        self.integer.is_some()
    }

    pub fn get_integer(&self) -> i32 {
        self.integer.unwrap_or(0)
    }

    pub fn get_list(&self) -> &Vec<NestedInteger> {
        &self.list
    }
}

struct Frame<'a> {
    node: &'a NestedInteger,
    index: usize,
}

pub struct NestedIterator<'a> {
    stack: Vec<Frame<'a>>,
}

impl<'a> NestedIterator<'a> {
    pub fn new(nested_list: &'a Vec<NestedInteger>) -> Self {
        let mut stack = Vec::new();
        for index in (0..nested_list.len()).rev() {
            stack.push(Frame {
                node: &nested_list[index],
                index: 0,
            });
        }
        NestedIterator { stack }
    }

    fn prepare_next(&mut self) {
        loop {
            if self.stack.is_empty() {
                return;
            }
            let needs_pop = {
                let top = &self.stack[self.stack.len() - 1];
                if top.node.is_integer() {
                    return;
                }
                top.index >= top.node.get_list().len()
            };
            if needs_pop {
                self.stack.pop();
                continue;
            }
            let child = {
                let top = &mut self.stack[self.stack.len() - 1];
                let child = &top.node.get_list()[top.index];
                top.index += 1;
                child
            };
            self.stack.push(Frame { node: child, index: 0 });
        }
    }

    fn advance(&mut self, nested: &[NestedInteger]) -> i32 {
        for index in (0..nested.len()).rev() {
            self.stack.push(Frame {
                node: &nested[index],
                index: 0,
            });
        }
        self.prepare_next();
        let current = self.stack.pop().unwrap();
        if current.node.is_integer() {
            return current.node.get_integer();
        }
        self.advance(current.node.get_list())
    }

    pub fn next(&mut self) -> i32 {
        let current = self.stack.pop().unwrap();
        if current.node.is_integer() {
            return current.node.get_integer();
        }
        self.advance(current.node.get_list())
    }

    pub fn has_next(&mut self) -> bool {
        self.prepare_next();
        !self.stack.is_empty()
    }
}
