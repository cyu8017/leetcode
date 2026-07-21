// LeetCode 1894 - Find the Student that Will Replace the Chalk
// https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

class Solution {
    func chalkReplacer(_ chalk: [Int], _ k: Int) -> Int {
        var k = k % chalk.reduce(0, +)
        for (index, need) in chalk.enumerated() {
            if k < need {
                return index
            }
            k -= need
        }
        return 0
    }
}
