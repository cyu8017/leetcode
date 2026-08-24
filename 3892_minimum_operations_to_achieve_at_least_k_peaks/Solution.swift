// LeetCode 3892 - Minimum Operations to Achieve At Least K Peaks
// https://leetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/

class Solution {
    private var cost = [Int]()
    private let INF = 1 << 60

    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        if k == 0 { return 0 }
        if k > n / 2 { return -1 }
        cost = [Int](repeating: 0, count: n)
        for i in 0..<n {
            let left = nums[(i + n - 1) % n], right = nums[(i + 1) % n]
            let need = max(left, right)
            if need >= nums[i] { cost[i] = need - nums[i] + 1 }
        }
        var answer = line(1, n - 1, k)
        var withFirst = line(2, n - 2, k - 1)
        if withFirst != INF {
            withFirst += cost[0]
            answer = min(answer, withFirst)
        }
        if answer == INF { return -1 }
        return answer
    }

    private func line(_ left: Int, _ right: Int, _ choose: Int) -> Int {
        if choose == 0 { return 0 }
        if left > right || choose > (right - left + 2) / 2 { return INF }
        var prev2 = [Int](repeating: INF, count: choose + 1)
        var prev1 = [Int](repeating: INF, count: choose + 1)
        prev2[0] = 0
        prev1[0] = 0
        if left <= right {
            for i in left...right {
                var current = prev1
                for j in 1...choose {
                    if prev2[j - 1] != INF && prev2[j - 1] + cost[i] < current[j] {
                        current[j] = prev2[j - 1] + cost[i]
                    }
                }
                prev2 = prev1
                prev1 = current
            }
        }
        return prev1[choose]
    }
}
