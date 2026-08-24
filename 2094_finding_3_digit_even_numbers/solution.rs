// LeetCode 2094 - Finding 3-Digit Even Numbers
// https://leetcode.com/problems/finding-3-digit-even-numbers/

impl Solution {
    pub fn find_even_numbers(digits: Vec<i32>) -> Vec<i32> {
        let mut freq = [0i32; 10];
        for d in digits {
            freq[d as usize] += 1;
        }
        let mut ans = Vec::new();
        let mut x = 100;
        while x <= 998 {
            let a = x / 100;
            let b = (x / 10) % 10;
            let c = x % 10;
            freq[a] -= 1;
            freq[b] -= 1;
            freq[c] -= 1;
            if freq[a] >= 0 && freq[b] >= 0 && freq[c] >= 0 {
                ans.push(x as i32);
            }
            freq[a] += 1;
            freq[b] += 1;
            freq[c] += 1;
            x += 2;
        }
        ans
    }
}
