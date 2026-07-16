// LeetCode 0193 - Valid Phone Numbers
// https://leetcode.com/problems/valid-phone-numbers/

const SCRIPT: &str = r#"
#!/bin/bash
grep -E '^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$' file.txt
"#;
