// LeetCode 1803 - Count Pairs With XOR in a Range
// https://leetcode.com/problems/count-pairs-with-xor-in-a-range/

private class XORTrieNode {
    var count = 0
    var children: [XORTrieNode?] = [nil, nil]
}

class Solution {
    func countPairs(_ nums: [Int], _ low: Int, _ high: Int) -> Int {
        return countSmallerThan(nums, high + 1) - countSmallerThan(nums, low)
    }

    private func countSmallerThan(_ nums: [Int], _ limit: Int) -> Int {
        if limit <= 0 { return 0 }
        let root = XORTrieNode()
        var total = 0
        let maxBit = 15
        for num in nums {
            total += query(root, num, limit, maxBit)
            insert(root, num, maxBit)
        }
        return total
    }

    private func insert(_ root: XORTrieNode, _ num: Int, _ bit: Int) {
        var node = root
        var i = bit
        while i >= 0 {
            let b = (num >> i) & 1
            if node.children[b] == nil {
                node.children[b] = XORTrieNode()
            }
            node = node.children[b]!
            node.count += 1
            i -= 1
        }
    }

    private func query(_ root: XORTrieNode?, _ num: Int, _ limit: Int, _ bit: Int) -> Int {
        guard let root = root, bit >= 0 else { return 0 }
        let numBit = (num >> bit) & 1
        let limitBit = (limit >> bit) & 1
        let child = root.children[numBit]
        if limitBit == 1 {
            let same = child?.count ?? 0
            return same + query(root.children[1 - numBit], num, limit, bit - 1)
        }
        return query(child, num, limit, bit - 1)
    }
}
