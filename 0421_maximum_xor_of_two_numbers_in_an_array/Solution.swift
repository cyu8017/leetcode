// LeetCode 0421 - Maximum XOR of Two Numbers in an Array
// https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution {
    private final class TrieNode {
        var children: [Int: TrieNode] = [:]
    }

    func findMaximumXOR(_ nums: [Int]) -> Int {
        let maximum = nums.max() ?? 0
        let maxBit = maximum == 0 ? 0 : Int.bitWidth - maximum.leadingZeroBitCount
        let root = TrieNode()
        var best = 0

        for number in nums {
            var node = root
            if maxBit > 0 {
                for bit in stride(from: maxBit - 1, through: 0, by: -1) {
                    let current = (number >> bit) & 1
                    if node.children[current] == nil {
                        node.children[current] = TrieNode()
                    }
                    node = node.children[current]!
                }
            }
        }

        for number in nums {
            var node = root
            var candidate = 0
            if maxBit > 0 {
                for bit in stride(from: maxBit - 1, through: 0, by: -1) {
                    let current = (number >> bit) & 1
                    let target = 1 - current
                    if node.children[target] != nil {
                        candidate |= 1 << bit
                        node = node.children[target]!
                    } else {
                        node = node.children[current]!
                    }
                }
            }
            best = max(best, candidate)
        }

        return best
    }
}
