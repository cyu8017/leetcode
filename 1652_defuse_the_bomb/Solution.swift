// LeetCode 1652 - Defuse the Bomb
// https://leetcode.com/problems/defuse-the-bomb/

class Solution {
    func decrypt(_ code: [Int], _ k: Int) -> [Int] {
        let n = code.count
        if k == 0 { return Array(repeating: 0, count: n) }
        let a = code + code
        var ans = [Int]()
        for i in 0..<n {
            var sum = 0
            if k > 0 {
                for j in (i + 1)...(i + k) { sum += a[j] }
            } else {
                for j in (i + n + k)..<(i + n) { sum += a[j] }
            }
            ans.append(sum)
        }
        return ans
    }
}
