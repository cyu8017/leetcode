// LeetCode 3991 - Sort Array Using Prefix Reversals
// https://leetcode.com/problems/sort-array-using-prefix-reversals/

class Solution {
    func sortArray(_ nums: [Int], _ pre: [Int]) -> Int {
        let n = nums.count
        let start = nums.map(String.init).joined(separator: ",")
        let target = (0..<n).map(String.init).joined(separator: ",")
        if start == target { return 0 }

        let lengths = Array(Set(pre.filter { $0 >= 2 && $0 <= n })).sorted()
        var visited: Set<String> = [start]
        var queue: [[Int]] = [nums]
        var steps = 0

        while !queue.isEmpty {
            steps += 1
            var nextQueue: [[Int]] = []
            for cur in queue {
                for i in lengths {
                    var nxt = cur
                    var l = 0
                    var r = i - 1
                    while l < r {
                        nxt.swapAt(l, r)
                        l += 1
                        r -= 1
                    }
                    let key = nxt.map(String.init).joined(separator: ",")
                    if key == target { return steps }
                    if visited.insert(key).inserted {
                        nextQueue.append(nxt)
                    }
                }
            }
            queue = nextQueue
        }
        return -1
    }
}
