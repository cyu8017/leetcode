// LeetCode 2269 - Find the K-Beauty of a Number
// https://leetcode.com/problems/find-the-k-beauty-of-a-number/

class Solution {
    func divisorSubstrings(_ num: Int, _ k: Int) -> Int {
        let s = Array(String(num))
        var ans = 0
        if s.count >= k {
            for i in 0...(s.count - k) {
                var sub = 0
                for j in 0..<k { sub = sub * 10 + Int(String(s[i + j]))! }
                if sub != 0 && num % sub == 0 { ans += 1 }
            }
        }
        return ans
    }
}
