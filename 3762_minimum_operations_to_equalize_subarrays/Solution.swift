// LeetCode 3762 - Minimum Operations To Equalize Subarrays
// https://leetcode.com/problems/minimum-operations-to-equalize-subarrays/

class Solution {
    private class Node {
        var left = 0, right = 0, count = 0
        var sum = 0
        init() {}
        init(_ o: Node) {
            left = o.left; right = o.right; count = o.count; sum = o.sum
        }
    }

    private var nodes = [Node]()

    func minOperations(_ nums: [Int], _ k: Int, _ queries: [[Int]]) -> [Int] {
        let n = nums.count
        var quotient = [Int](repeating: 0, count: n)
        var remainder = [Int](repeating: 0, count: n)
        var values = [Int](repeating: 0, count: n)
        for i in 0..<n {
            quotient[i] = nums[i] / k
            remainder[i] = nums[i] % k
            values[i] = quotient[i]
        }
        values.sort()
        var vu = 1
        if n > 1 {
            for i in 1..<n {
                if values[i] != values[vu - 1] {
                    values[vu] = values[i]
                    vu += 1
                }
            }
        }
        values = Array(values.prefix(vu))

        nodes = [Node()]
        var roots = [Int](repeating: 0, count: n + 1)
        let umax = values.count - 1
        for i in 0..<n {
            let position = lowerBound(values, quotient[i])
            roots[i + 1] = update(roots[i], 0, umax, position, quotient[i])
        }

        var logv = [Int](repeating: 0, count: n + 1)
        if n >= 2 {
            for i in 2...n { logv[i] = logv[i / 2] + 1 }
        }
        let levels = logv[n] + 1
        var minTable = [[Int]](repeating: [], count: levels)
        var maxTable = [[Int]](repeating: [], count: levels)
        minTable[0] = remainder
        maxTable[0] = remainder
        if levels > 1 {
            for level in 1..<levels {
                let length = n - (1 << level) + 1
                minTable[level] = [Int](repeating: 0, count: length)
                maxTable[level] = [Int](repeating: 0, count: length)
                let half = 1 << (level - 1)
                if length > 0 {
                    for i in 0..<length {
                        minTable[level][i] = min(minTable[level - 1][i], minTable[level - 1][i + half])
                        maxTable[level][i] = max(maxTable[level - 1][i], maxTable[level - 1][i + half])
                    }
                }
            }
        }

        var answer = [Int](repeating: 0, count: queries.count)
        for qi in 0..<queries.count {
            let left = queries[qi][0], right = queries[qi][1]
            let length = right - left + 1
            let level = logv[length]
            let offset = right - (1 << level) + 1
            let minR = min(minTable[level][left], minTable[level][offset])
            let maxR = max(maxTable[level][left], maxTable[level][offset])
            if minR != maxR {
                answer[qi] = -1
                continue
            }
            let medianIndex = kth(roots[right + 1], roots[left], 0, umax, (length + 1) / 2)
            let median = values[medianIndex]
            let stats = prefixStats(roots[right + 1], roots[left], 0, umax, medianIndex)
            let leftCount = stats.0
            let leftSum = stats.1
            let totalSum = nodes[roots[right + 1]].sum - nodes[roots[left]].sum
            answer[qi] = median * leftCount - leftSum + (totalSum - leftSum) - median * (length - leftCount)
        }
        return answer
    }

    private func update(_ previous: Int, _ lo: Int, _ hi: Int, _ position: Int, _ value: Int) -> Int {
        let current = nodes.count
        nodes.append(Node(nodes[previous]))
        nodes[current].count += 1
        nodes[current].sum += value
        if lo < hi {
            let mid = (lo + hi) / 2
            if position <= mid {
                nodes[current].left = update(nodes[previous].left, lo, mid, position, value)
            } else {
                nodes[current].right = update(nodes[previous].right, mid + 1, hi, position, value)
            }
        }
        return current
    }

    private func kth(_ rightRoot: Int, _ leftRoot: Int, _ lo: Int, _ hi: Int, _ rank: Int) -> Int {
        if lo == hi { return lo }
        let leftCount = nodes[nodes[rightRoot].left].count - nodes[nodes[leftRoot].left].count
        let mid = (lo + hi) / 2
        if rank <= leftCount { return kth(nodes[rightRoot].left, nodes[leftRoot].left, lo, mid, rank) }
        return kth(nodes[rightRoot].right, nodes[leftRoot].right, mid + 1, hi, rank - leftCount)
    }

    private func prefixStats(_ rightRoot: Int, _ leftRoot: Int, _ lo: Int, _ hi: Int, _ end: Int) -> (Int, Int) {
        if end < lo { return (0, 0) }
        if hi <= end {
            return (nodes[rightRoot].count - nodes[leftRoot].count,
                    nodes[rightRoot].sum - nodes[leftRoot].sum)
        }
        let mid = (lo + hi) / 2
        var left = prefixStats(nodes[rightRoot].left, nodes[leftRoot].left, lo, mid, end)
        if end > mid {
            let right = prefixStats(nodes[rightRoot].right, nodes[leftRoot].right, mid + 1, hi, end)
            left.0 += right.0
            left.1 += right.1
        }
        return left
    }

    private func lowerBound(_ a: [Int], _ x: Int) -> Int {
        var lo = 0, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] < x { lo = mid + 1 }
            else { hi = mid }
        }
        return lo
    }
}
