// LeetCode 0444 - Sequence Reconstruction
// https://leetcode.com/problems/sequence-reconstruction/

class Solution {
    func sequenceReconstruction(_ nums: [Int], _ sequences: [[Int]]) -> Bool {
        var indegree = Dictionary(uniqueKeysWithValues: nums.map { ($0, 0) })
        var graph = Dictionary(uniqueKeysWithValues: nums.map { ($0, Set<Int>()) })
        var seenEdges = Set<[Int]>()

        for sequence in sequences {
            for index in 0..<(sequence.count - 1) {
                let left = sequence[index]
                let right = sequence[index + 1]
                if seenEdges.contains([left, right]) {
                    continue
                }
                seenEdges.insert([left, right])
                graph[left, default: []].insert(right)
                indegree[right, default: 0] += 1
            }
        }

        var queue = nums.filter { indegree[$0, default: 0] == 0 }
        var order: [Int] = []
        while !queue.isEmpty {
            if queue.count > 1 {
                return false
            }
            let node = queue.removeFirst()
            order.append(node)
            for neighbor in graph[node, default: []] {
                indegree[neighbor, default: 0] -= 1
                if indegree[neighbor, default: 0] == 0 {
                    queue.append(neighbor)
                }
            }
        }

        return order == nums
    }
}
