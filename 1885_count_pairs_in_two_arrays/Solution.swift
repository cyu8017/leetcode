// LeetCode 1885 - Count Pairs in Two Arrays
// https://leetcode.com/problems/count-pairs-in-two-arrays/

class Solution {
    func countPairs(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let diff = zip(nums1, nums2).map { $0 - $1 }.sorted()
        let n = diff.count
        var answer = 0

        for i in 0..<n {
            let target = -diff[i]
            answer += n - upperBound(diff, target, from: i + 1)
        }

        return answer
    }

    private func upperBound(_ arr: [Int], _ target: Int, from start: Int) -> Int {
        var lo = start
        var hi = arr.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if arr[mid] <= target {
                lo = mid + 1
            } else {
                hi = mid
            }
        }
        return lo
    }
}
