// LeetCode 3845 - Maximum Subarray XOR with Bounded Range
// https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/

class Solution {
    private class Node {
        var next = [0, 0]
        var count = 0
    }

    private var nodes = [Node]()

    private func add(_ x: Int, _ delta: Int) {
        var u = 0
        nodes[u].count += delta
        for b in stride(from: 15, through: 0, by: -1) {
            let bit = (x >> b) & 1
            if nodes[u].next[bit] == 0 {
                nodes[u].next[bit] = nodes.count
                nodes.append(Node())
            }
            u = nodes[u].next[bit]
            nodes[u].count += delta
        }
    }

    private func query(_ x: Int) -> Int {
        var u = 0, res = 0
        for b in stride(from: 15, through: 0, by: -1) {
            let bit = (x >> b) & 1
            let want = bit ^ 1
            let v = nodes[u].next[want]
            if v != 0 && nodes[v].count > 0 {
                res |= 1 << b
                u = v
            } else {
                u = nodes[u].next[bit]
            }
        }
        return res
    }

    func maxSubarrayXor(_ nums: [Int], _ k: Int) -> Int {
        nodes = [Node()]
        let n = nums.count
        var pref = [Int](repeating: 0, count: n + 1)
        for i in 0..<n { pref[i + 1] = pref[i] ^ nums[i] }
        var maxQ = [Int]()
        var minQ = [Int]()
        var left = 0, trieLeft = 0, ans = 0
        for r in 0..<n {
            let x = nums[r]
            while !maxQ.isEmpty && nums[maxQ.last!] <= x { maxQ.removeLast() }
            maxQ.append(r)
            while !minQ.isEmpty && nums[minQ.last!] >= x { minQ.removeLast() }
            minQ.append(r)
            while nums[maxQ[0]] - nums[minQ[0]] > k {
                if maxQ[0] == left { maxQ.removeFirst() }
                if minQ[0] == left { minQ.removeFirst() }
                left += 1
            }
            add(pref[r], 1)
            while trieLeft < left {
                add(pref[trieLeft], -1)
                trieLeft += 1
            }
            let cur = query(pref[r + 1])
            if cur > ans { ans = cur }
        }
        return ans
    }
}
