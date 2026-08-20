// LeetCode 1405 - Longest Happy String
// https://leetcode.com/problems/longest-happy-string/

class Solution {
    func longestDiverseString(_ a: Int, _ b: Int, _ c: Int) -> String {
        var heap = [(a, Character("a")), (b, Character("b")), (c, Character("c"))].filter { $0.0 > 0 }
        var answer = [Character]()
        while !heap.isEmpty {
            heap.sort { $0.0 > $1.0 }
            var (count, char) = heap.removeFirst()
            if answer.count >= 2 && answer[answer.count - 1] == char && answer[answer.count - 2] == char {
                if heap.isEmpty { break }
                heap.sort { $0.0 > $1.0 }
                var (count2, char2) = heap.removeFirst()
                answer.append(char2)
                count2 -= 1
                if count2 > 0 { heap.append((count2, char2)) }
                heap.append((count, char))
            } else {
                answer.append(char)
                count -= 1
                if count > 0 { heap.append((count, char)) }
            }
        }
        return String(answer)
    }
}
