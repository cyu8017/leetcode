// LeetCode 3806 - Maximum Bitwise And After Increment Operations
// https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/

class Solution {
    private func bitLen(_ x: Int) -> Int {
        if x == 0 { return 0 }
        var x = x, n = 0
        while x > 0 { n += 1; x >>= 1 }
        return n
    }

    func maximumAND(_ nums: [Int], _ k: Int, _ m: Int) -> Int {
        var mxVal = nums[0]
        for v in nums where v > mxVal { mxVal = v }
        mxVal += k
        let mx = bitLen(mxVal)
        var ans = 0
        var cost = [Int](repeating: 0, count: nums.count)
        if mx > 0 {
            for bit in stride(from: mx - 1, through: 0, by: -1) {
                let target = ans | (1 << bit)
                for i in 0..<nums.count {
                    let x = nums[i]
                    let j = bitLen(target & ~x)
                    let mask = (1 << j) - 1
                    cost[i] = (target & mask) - (x & mask)
                }
                cost.sort()
                var sum = 0
                for i in 0..<m { sum += cost[i] }
                if sum <= k { ans = target }
            }
        }
        return ans
    }
}
