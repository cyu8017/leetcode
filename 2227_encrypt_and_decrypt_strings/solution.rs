// LeetCode 2227 - Encrypt and Decrypt Strings
// https://leetcode.com/problems/encrypt-and-decrypt-strings/

use std::collections::HashMap;

pub struct Encrypter {
    enc: HashMap<char, String>,
    cnt: HashMap<String, i32>,
}

impl Encrypter {
    pub fn new(keys: Vec<char>, values: Vec<String>, dictionary: Vec<String>) -> Self {
        let mut enc = HashMap::new();
        for i in 0..keys.len() {
            enc.insert(keys[i], values[i].clone());
        }
        let mut this = Self {
            enc,
            cnt: HashMap::new(),
        };
        for w in dictionary {
            let e = this.encrypt(w);
            *this.cnt.entry(e).or_insert(0) += 1;
        }
        this
    }

    pub fn encrypt(&self, word1: String) -> String {
        let mut b = String::new();
        for c in word1.chars() {
            match self.enc.get(&c) {
                Some(v) => b.push_str(v),
                None => return String::new(),
            }
        }
        b
    }

    pub fn decrypt(&self, word2: String) -> i32 {
        *self.cnt.get(&word2).unwrap_or(&0)
    }
}
