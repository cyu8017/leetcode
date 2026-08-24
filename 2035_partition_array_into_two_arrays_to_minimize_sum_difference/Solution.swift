// LeetCode 2035 - Partition Array Into Two Arrays to Minimize Sum Difference
// https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/

class Solution {
    func minimumDifference(_ nums: [Int]) -> Int {
        let n = nums.count / 2
        let total = nums.reduce(0, +)
        let left = Array(nums[0..<n])
        let right = Array(nums[n...])
        let L = sumsByCount(left)
        let R = sumsByCount(right)
        var ans = Int.max
        for k in 0...n {
            for s1 in L[k] {
                let need = total / 2 - s1
                let arr = R[n - k]
                var lo = 0, hi = arr.count
                while lo < hi {
                    let mid = (lo + hi) / 2
                    if arr[mid] < need { lo = mid + 1 }
                    else { hi = mid }
                }
                for j in [lo - 1, lo] where j >= 0 && j < arr.count {
                    ans = min(ans, abs(total - 2 * (s1 + arr[j])))
                }
            }
        }
        return ans
    }

    private func sumsByCount(_ arr: [Int]) -> [[Int]] {
        let m = arr.count
        var res = [[Int]](repeating: [], count: m + 1)
        for mask in 0..<(1 << m) {
            var sum = 0, c = 0
            for i in 0..<m where (mask & (1 << i)) != 0 {
                sum += arr[i]
                c += 1
            }
            res[c].append(sum)
        }
        for i in 0...m { res[i].sort() }
        return res
    }
}
