// LeetCode 3015 - Count the Number of Houses at a Certain Distance I
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/

class Solution {
    func countOfPairs(_ n: Int, _ x0: Int, _ y0: Int) -> [Int] {
        var ans = Array(repeating: 0, count: n)
        let x = x0 - 1, y = y0 - 1
        for i in 0..<n {
            for j in (i + 1)..<n {
                let a = j - i
                let b = abs(x - i) + abs(y - j) + 1
                let c = abs(x - j) + abs(y - i) + 1
                ans[min(a, min(b, c)) - 1] += 2
            }
        }
        return ans
    }
}
