// LeetCode 0526 - Beautiful Arrangement
// https://leetcode.com/problems/beautiful-arrangement/

class Solution {
    func countArrangement(_ n: Int) -> Int {
        var count = 0

        func backtrack(_ index: Int, _ used: inout Set<Int>) {
            if index == n + 1 {
                count += 1
                return
            }
            for num in 1...n {
                if used.contains(num) {
                    continue
                }
                if index % num != 0 && num % index != 0 {
                    continue
                }
                used.insert(num)
                backtrack(index + 1, &used)
                used.remove(num)
            }
        }

        var used: Set<Int> = []
        backtrack(1, &used)
        return count
    }
}
