// LeetCode 3962 - Maximum Subarray Sum After at Most K Swaps
// https://leetcode.com/problems/maximum-subarray-sum-after-at-most-k-swaps/


class Solution {
    private var unique: [Int] = []

    func maxSubarraySum(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        unique = nums.sorted()
        var u = 0
        for i in 0..<unique.count {
            if u == 0 || unique[i] != unique[u - 1] {
                unique[u] = unique[i]
                u += 1
            }
        }
        unique = Array(unique.prefix(u))
        var rank = Array(repeating: 0, count: n)
        var globalCount = Array(repeating: 0, count: unique.count + 1)
        var globalSum = Array(repeating: 0, count: unique.count + 1)
        for i in 0..<n {
            rank[i] = lowerBound(unique, nums[i]) + 1
            add(&globalCount, &globalSum, rank[i], 1)
        }
        var answer = -(Int.max / 4)
        for left in 0..<n {
            var insideCount = Array(repeating: 0, count: unique.count + 1)
            var insideSum = Array(repeating: 0, count: unique.count + 1)
            var outsideCount = globalCount
            var outsideSum = globalSum
            var subarraySum = 0
            for right in left..<n {
                add(&outsideCount, &outsideSum, rank[right], -1)
                add(&insideCount, &insideSum, rank[right], 1)
                subarraySum += nums[right]
                let insideSize = right - left + 1
                let outsideSize = n - insideSize
                let limit = min(k, min(insideSize, outsideSize))
                var low = 0, high = limit
                while low < high {
                    let mid = (low + high + 1) / 2
                    let insideValue = unique[kth(insideCount, mid) - 1]
                    let outsideOrder = outsideSize - mid + 1
                    let outsideValue = unique[kth(outsideCount, outsideOrder) - 1]
                    if outsideValue > insideValue { low = mid }
                    else { high = mid - 1 }
                }
                let swaps = low
                var gain = 0
                if swaps > 0 {
                    let smallInside = sumSmallest(insideCount, insideSum, swaps)
                    let totalOutside = querySum(outsideSum, unique.count)
                    let largeOutside = totalOutside - sumSmallest(outsideCount, outsideSum, outsideSize - swaps)
                    gain = largeOutside - smallInside
                }
                answer = max(answer, subarraySum + gain)
            }
        }
        return answer
    }

    private func add(_ count: inout [Int], _ sum: inout [Int], _ index0: Int, _ delta: Int) {
        var index = index0
        let value = unique[index - 1]
        while index < count.count {
            count[index] += delta
            sum[index] += delta * value
            index += index & -index
        }
    }

    private func queryCount(_ bit: [Int], _ index0: Int) -> Int {
        var index = index0, result = 0
        while index > 0 {
            result += bit[index]
            index -= index & -index
        }
        return result
    }

    private func querySum(_ bit: [Int], _ index0: Int) -> Int {
        var index = index0, result = 0
        while index > 0 {
            result += bit[index]
            index -= index & -index
        }
        return result
    }

    private func kth(_ bit: [Int], _ order0: Int) -> Int {
        var order = order0, index = 0, step = 1
        while (step << 1) < bit.count { step <<= 1 }
        while step > 0 {
            let next = index + step
            if next < bit.count && bit[next] < order {
                index = next
                order -= bit[next]
            }
            step >>= 1
        }
        return index + 1
    }

    private func sumSmallest(_ count: [Int], _ sum: [Int], _ amount: Int) -> Int {
        if amount <= 0 { return 0 }
        let index = kth(count, amount)
        let countBefore = queryCount(count, index - 1)
        let sumBefore = querySum(sum, index - 1)
        return sumBefore + (amount - countBefore) * unique[index - 1]
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
