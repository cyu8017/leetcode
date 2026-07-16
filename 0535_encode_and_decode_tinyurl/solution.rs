// LeetCode 0535 - Encode and Decode TinyURL
// https://leetcode.com/problems/encode-and-decode-tinyurl/

use std::collections::HashMap;

pub struct Codec {
    url_to_code: HashMap<String, String>,
    code_to_url: HashMap<String, String>,
    counter: i32,
    base: String,
}

impl Codec {
    pub fn new() -> Self {
        Codec {
            url_to_code: HashMap::new(),
            code_to_url: HashMap::new(),
            counter: 0,
            base: "http://tinyurl.com/".to_string(),
        }
    }

    pub fn encode(&mut self, long_url: String) -> String {
        if let Some(short_url) = self.url_to_code.get(&long_url) {
            return short_url.clone();
        }
        let code = self.counter.to_string();
        self.counter += 1;
        let short_url = format!("{}{}", self.base, code);
        self.url_to_code.insert(long_url.clone(), short_url.clone());
        self.code_to_url.insert(short_url.clone(), long_url);
        short_url
    }

    pub fn decode(&self, short_url: String) -> String {
        self.code_to_url.get(&short_url).cloned().unwrap()
    }
}
