// LeetCode 0385 - Mini Parser
// https://leetcode.com/problems/mini-parser/

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

impl Solution {
    pub fn deserialize(s: String) -> NestedInteger {
        if s.is_empty() || !s.starts_with('[') {
            return NestedInteger::new(s.parse().ok());
        }

        let chars: Vec<char> = s.chars().collect();
        let mut stack: Vec<NestedInteger> = Vec::new();
        let mut current = NestedInteger::new(None);
        let mut index = 0;
        let mut negative = false;
        let mut number = 0;
        let mut has_number = false;

        while index < chars.len() {
            match chars[index] {
                '[' => {
                    let item = NestedInteger::new(None);
                    if !stack.is_empty() || !current.list.is_empty() || current.integer.is_some() {
                        stack.push(current);
                    }
                    current = item;
                }
                '-' => negative = true,
                '0'..='9' => {
                    number = number * 10 + chars[index].to_digit(10).unwrap() as i32;
                    has_number = true;
                }
                ',' | ']' => {
                    if has_number {
                        let value = if negative { -number } else { number };
                        current.list.push(NestedInteger::new(Some(value)));
                        number = 0;
                        negative = false;
                        has_number = false;
                    }
                    if chars[index] == ']' {
                        if stack.is_empty() {
                            return current;
                        }
                        let mut parent = stack.pop().unwrap();
                        parent.list.push(current);
                        current = parent;
                    }
                }
                _ => {}
            }
            index += 1;
        }

        current
    }
}
