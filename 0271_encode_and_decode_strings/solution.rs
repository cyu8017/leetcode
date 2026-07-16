// LeetCode 0271 - Encode and Decode Strings
// https://leetcode.com/problems/encode-and-decode-strings/

struct Codec;

impl Codec {
    pub fn encode(&self, strs: Vec<String>) -> String {
        strs.iter()
            .map(|text| format!("{}#{}", text.len(), text))
            .collect()
    }

    pub fn decode(&self, encoded: String) -> Vec<String> {
        let mut result = Vec::new();
        let bytes = encoded.as_bytes();
        let mut index = 0;
        while index < bytes.len() {
            let delimiter = encoded[index..]
                .find('#')
                .map(|offset| index + offset)
                .unwrap_or(index);
            let length: usize = encoded[index..delimiter].parse().unwrap();
            let start = delimiter + 1;
            let end = start + length;
            result.push(encoded[start..end].to_string());
            index = end;
        }
        result
    }
}
