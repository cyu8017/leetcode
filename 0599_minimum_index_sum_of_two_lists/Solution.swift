// LeetCode 0599 - Minimum Index Sum of Two Lists
// https://leetcode.com/problems/minimum-index-sum-of-two-lists/

class Solution {
    func findRestaurant(_ list1: [String], _ list2: [String]) -> [String] {
        var index1 = [String: Int]()
        for (i, s) in list1.enumerated() { index1[s] = i }
        var best = Int.max
        var answer = [String]()
        for (j, s) in list2.enumerated() {
            guard let i = index1[s] else { continue }
            let total = i + j
            if total < best {
                best = total
                answer = [s]
            } else if total == best {
                answer.append(s)
            }
        }
        return answer
    }
}
