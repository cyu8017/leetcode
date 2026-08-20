// LeetCode 1409 - Queries on a Permutation With Key
// https://leetcode.com/problems/queries-on-a-permutation-with-key/

class Solution {
    func processQueries(_ queries: [Int], _ m: Int) -> [Int] {
        var values = Array(1...m), answer = [Int]()
        for query in queries {
            let index = values.firstIndex(of: query)!
            answer.append(index)
            values.insert(values.remove(at: index), at: 0)
        }
        return answer
    }
}
