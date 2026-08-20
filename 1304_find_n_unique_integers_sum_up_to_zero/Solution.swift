// LeetCode 1304 - Find N Unique Integers Sum up to Zero
// https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

class Solution {
    func sumZero(_ n: Int) -> [Int] {
        var answer = [Int]()
        if n / 2 > 0 {
            for value in 1...(n / 2) {
                answer.append(-value)
                answer.append(value)
            }
        }
        if n % 2 != 0 { answer.append(0) }
        return answer
    }
}
