// LeetCode 0770 - Basic Calculator IV
// https://leetcode.com/problems/basic-calculator-iv/

use std::collections::{BTreeMap, HashMap};

type Poly = BTreeMap<Vec<String>, i32>;

impl Solution {
    pub fn basic_calculator_iv(
        expression: String,
        evalvars: Vec<String>,
        evalints: Vec<i32>,
    ) -> Vec<String> {
        let mut values = HashMap::new();
        for (var, val) in evalvars.into_iter().zip(evalints.into_iter()) {
            values.insert(var, val);
        }
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
        let poly = Self::parse_expr(&tokens, &mut pos, &values);
        let mut keys: Vec<(Vec<String>, i32)> = poly.into_iter().collect();
        keys.sort_by(|a, b| {
            if a.0.len() != b.0.len() {
                b.0.len().cmp(&a.0.len())
            } else {
                a.0.cmp(&b.0)
            }
        });
        let mut answer = Vec::new();
        for (key, coef) in keys {
            if coef == 0 {
                continue;
            }
            if key.is_empty() {
                answer.push(coef.to_string());
            } else {
                let mut term = coef.to_string();
                for var in key {
                    term.push('*');
                    term.push_str(&var);
                }
                answer.push(term);
            }
        }
        answer
    }

    fn parse_expr(tokens: &[String], pos: &mut usize, values: &HashMap<String, i32>) -> Poly {
        let mut poly = Self::parse_term(tokens, pos, values);
        while *pos < tokens.len() && (tokens[*pos] == "+" || tokens[*pos] == "-") {
            let op = tokens[*pos].clone();
            *pos += 1;
            let right = Self::parse_term(tokens, pos, values);
            poly = if op == "+" {
                Self::add(&poly, &right)
            } else {
                Self::add(&poly, &Self::negate(&right))
            };
        }
        poly
    }

    fn parse_term(tokens: &[String], pos: &mut usize, values: &HashMap<String, i32>) -> Poly {
        let mut poly = Self::parse_factor(tokens, pos, values);
        while *pos < tokens.len() && tokens[*pos] == "*" {
            *pos += 1;
            poly = Self::mul(&poly, &Self::parse_factor(tokens, pos, values));
        }
        poly
    }

    fn parse_factor(tokens: &[String], pos: &mut usize, values: &HashMap<String, i32>) -> Poly {
        if tokens[*pos] == "(" {
            *pos += 1;
            let poly = Self::parse_expr(tokens, pos, values);
            *pos += 1;
            poly
        } else {
            let token = tokens[*pos].clone();
            *pos += 1;
            Self::atom(&token, values)
        }
    }

    fn atom(token: &str, values: &HashMap<String, i32>) -> Poly {
        let mut poly = Poly::new();
        if token.as_bytes()[0].is_ascii_alphabetic() {
            if let Some(&val) = values.get(token) {
                poly.insert(vec![], val);
            } else {
                poly.insert(vec![token.to_string()], 1);
            }
        } else {
            poly.insert(vec![], token.parse().unwrap());
        }
        Self::clean(poly)
    }

    fn add(left: &Poly, right: &Poly) -> Poly {
        let mut result = left.clone();
        for (key, coef) in right {
            *result.entry(key.clone()).or_insert(0) += coef;
        }
        Self::clean(result)
    }

    fn negate(poly: &Poly) -> Poly {
        poly.iter().map(|(k, v)| (k.clone(), -v)).collect()
    }

    fn mul(left: &Poly, right: &Poly) -> Poly {
        let mut result = Poly::new();
        for (lk, lv) in left {
            for (rk, rv) in right {
                let mut key = lk.clone();
                key.extend(rk.iter().cloned());
                key.sort();
                *result.entry(key).or_insert(0) += lv * rv;
            }
        }
        Self::clean(result)
    }

    fn clean(mut poly: Poly) -> Poly {
        poly.retain(|_, coef| *coef != 0);
        poly
    }
}
