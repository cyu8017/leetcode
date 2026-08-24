// LeetCode 2094 - Finding 3-Digit Even Numbers
// https://leetcode.com/problems/finding-3-digit-even-numbers/

class Solution {
    func findEvenNumbers(_ digits: [Int]) -> [Int] {
        var freq = [Int](repeating: 0, count: 10)
        for d in digits { freq[d] += 1 }
        var ans = [Int]()
        var x = 100
        while x <= 998 {
            let a = x / 100, b = (x / 10) % 10, c = x % 10
            freq[a] -= 1; freq[b] -= 1; freq[c] -= 1
            if freq[a] >= 0 && freq[b] >= 0 && freq[c] >= 0 { ans.append(x) }
            freq[a] += 1; freq[b] += 1; freq[c] += 1
            x += 2
        }
        return ans
    }
}
