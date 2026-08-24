// LeetCode 0736 - Parse Lisp Expression
// https://leetcode.com/problems/parse-lisp-expression/

use std::collections::HashMap;

impl Solution {
    pub fn evaluate(expression: String) -> i32 {
        let mut tokens = Vec::new();
        let mut cur = String::new();
        for ch in expression.chars() {
            if ch == '(' || ch == ')' {
                if !cur.is_empty() {
                    tokens.push(std::mem::take(&mut cur));
                }
                tokens.push(ch.to_string());
            } else if ch.is_whitespace() {
                if !cur.is_empty() {
                    tokens.push(std::mem::take(&mut cur));
                }
            } else {
                cur.push(ch);
            }
        }
        if !cur.is_empty() {
            tokens.push(cur);
        }
        let mut pos = 0;
        let mut env = Vec::new();
        Self::parse(&tokens, &mut pos, &mut env)
    }

    fn parse(
        tokens: &[String],
        pos: &mut usize,
        env: &mut Vec<HashMap<String, i32>>,
    ) -> i32 {
        let token = &tokens[*pos];
        if token != "(" {
            *pos += 1;
            if token.as_bytes()[0].is_ascii_digit()
                || (token.starts_with('-') && token.len() > 1)
            {
                return token.parse().unwrap();
            }
            for scope in env.iter().rev() {
                if let Some(&value) = scope.get(token) {
                    return value;
                }
            }
            return 0;
        }

        *pos += 1;
        let op = tokens[*pos].clone();
        *pos += 1;
        if op == "let" {
            env.push(HashMap::new());
            while tokens[*pos] != ")" {
                if tokens[*pos] == "(" || tokens[*pos + 1] == ")" {
                    let value = Self::parse(tokens, pos, env);
                    *pos += 1;
                    env.pop();
                    return value;
                }
                let var = tokens[*pos].clone();
                *pos += 1;
                let value = Self::parse(tokens, pos, env);
                env.last_mut().unwrap().insert(var, value);
            }
        }
        if op == "add" {
            let left = Self::parse(tokens, pos, env);
            let right = Self::parse(tokens, pos, env);
            *pos += 1;
            return left + right;
        }
        if op == "mult" {
            let left = Self::parse(tokens, pos, env);
            let right = Self::parse(tokens, pos, env);
            *pos += 1;
            return left * right;
        }
        0
    }
}
