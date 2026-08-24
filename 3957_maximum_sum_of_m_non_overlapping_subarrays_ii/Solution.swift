// LeetCode 3957 - Maximum Sum of M Non-Overlapping Subarrays II
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/


class Solution {
    private struct State {
        var value: Int
        var count: Int
        init() { value = 0; count = 0 }
        init(_ value: Int, _ count: Int) { self.value = value; self.count = count }
    }

    private func better(_ a: State, _ b: State) -> Bool {
        a.value > b.value || (a.value == b.value && a.count > b.count)
    }

    func maxSum(_ nums: [Int], _ m: Int, _ l: Int, _ r: Int) -> Int {
        let n = nums.count
        var prefix = Array(repeating: 0, count: n + 1)
        for i in 0..<n { prefix[i + 1] = prefix[i] + nums[i] }
        let unconstrained = run(prefix, n, l, r, 0)
        if unconstrained.count > 0 && unconstrained.count <= m { return unconstrained.value }
        if unconstrained.count > m {
            var bound = 0
            for value in nums { bound += value >= 0 ? value : -value }
            var low = 0, high = bound + 1
            while low < high {
                let mid = low + (high - low + 1) / 2
                if run(prefix, n, l, r, mid).count >= m { low = mid }
                else { high = mid - 1 }
            }
            let state = run(prefix, n, l, r, low)
            return state.value + low * m
        }
        let infinity = Int.max / 4
        var bestSingle = -infinity
        var deque = [Int]()
        for end in 1...n {
            let addIndex = end - l
            if addIndex >= 0 {
                while !deque.isEmpty && prefix[deque.last!] >= prefix[addIndex] { deque.removeLast() }
                deque.append(addIndex)
            }
            let minIndex = end - r
            while !deque.isEmpty && deque[0] < minIndex { deque.removeFirst() }
            if !deque.isEmpty {
                let sum = prefix[end] - prefix[deque[0]]
                if sum > bestSingle { bestSingle = sum }
            }
        }
        return bestSingle
    }

    private func run(_ prefix: [Int], _ n: Int, _ l: Int, _ r: Int, _ penalty: Int) -> State {
        var dp = Array(repeating: State(), count: n + 1)
        var deque = [Int]()
        for end in 1...n {
            let addIndex = end - l
            if addIndex >= 0 {
                while !deque.isEmpty && candidateBetter(dp, prefix, addIndex, deque.last!) { deque.removeLast() }
                deque.append(addIndex)
            }
            let minIndex = end - r
            while !deque.isEmpty && deque[0] < minIndex { deque.removeFirst() }
            dp[end] = State(dp[end - 1].value, dp[end - 1].count)
            if !deque.isEmpty {
                let start = deque[0]
                let take = State(dp[start].value + prefix[end] - prefix[start] - penalty, dp[start].count + 1)
                if better(take, dp[end]) { dp[end] = take }
            }
        }
        return dp[n]
    }

    private func candidateBetter(_ dp: [State], _ prefix: [Int], _ a: Int, _ b: Int) -> Bool {
        let left = State(dp[a].value - prefix[a], dp[a].count)
        let right = State(dp[b].value - prefix[b], dp[b].count)
        return better(left, right)
    }
}
