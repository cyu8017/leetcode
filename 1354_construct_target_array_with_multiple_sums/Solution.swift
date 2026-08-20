// LeetCode 1354 - Construct Target Array With Multiple Sums
// https://leetcode.com/problems/construct-target-array-with-multiple-sums/

class Solution {
    func isPossible(_ target: [Int]) -> Bool {
        if target.count == 1 { return target[0] == 1 }
        var heap = target // max-heap via negatives simulation with sort each time for simplicity
        var total = target.reduce(0, +)
        while true {
            heap.sort()
            let x = heap.removeLast()
            let rest = total - x
            if x == 1 || rest == 1 { return true }
            if rest == 0 || x <= rest { return false }
            let prev = x % rest
            if prev == 0 { return false }
            total = rest + prev
            heap.append(prev)
        }
    }
}
