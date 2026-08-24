// LeetCode 3483 - Unique 3-Digit Even Numbers
// https://leetcode.com/problems/unique-3-digit-even-numbers/

class Solution {
    func totalNumbers(_ digits: [Int]) -> Int {
        var seen = Set<Int>()
        let n = digits.count
        for i in 0..<n {
            for j in 0..<n where j != i {
                for k in 0..<n where k != i && k != j {
                    if digits[i] == 0 { continue }
                    if digits[k] % 2 != 0 { continue }
                    seen.insert(digits[i] * 100 + digits[j] * 10 + digits[k])
                }
            }
        }
        return seen.count
    }
}
