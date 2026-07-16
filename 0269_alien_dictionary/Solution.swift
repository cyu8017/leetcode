// LeetCode 0269 - Alien Dictionary
// https://leetcode.com/problems/alien-dictionary/

class Solution {
    func alienOrder(_ words: [String]) -> String {
        var graph: [Character: Set<Character>] = [:]
        var indegree: [Character: Int] = [:]

        for word in words {
            for char in word {
                if graph[char] == nil {
                    graph[char] = []
                    indegree[char] = 0
                }
            }
        }

        for index in 0..<(words.count - 1) {
            let first = words[index]
            let second = words[index + 1]
            if first.count > second.count && first.hasPrefix(second) {
                return ""
            }
            let limit = min(first.count, second.count)
            for offset in 0..<limit {
                let left = first[first.index(first.startIndex, offsetBy: offset)]
                let right = second[second.index(second.startIndex, offsetBy: offset)]
                if left != right {
                    if !graph[left]!.contains(right) {
                        graph[left]!.insert(right)
                        indegree[right, default: 0] += 1
                    }
                    break
                }
            }
        }

        var queue: [Character] = []
        for (char, degree) in indegree where degree == 0 {
            queue.append(char)
        }

        var order = ""
        while !queue.isEmpty {
            let char = queue.removeFirst()
            order.append(char)
            for next in graph[char] ?? [] {
                indegree[next]! -= 1
                if indegree[next] == 0 {
                    queue.append(next)
                }
            }
        }

        return order.count == indegree.count ? order : ""
    }
}
