// LeetCode 3134 - Find the Median of the Uniqueness Array
// https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/

class Solution {
    func medianOfUniquenessArray(_ nums: [Int]) -> Int {
        let n = nums.count
        let m = (1 + n) * n / 2
        var lo = 1, hi = n
        while lo < hi {
            let mid = lo + (hi - lo) / 2
            if check(nums, n, m, mid) { hi = mid }
            else { lo = mid + 1 }
        }
        return lo
    }

    private func check(_ nums: [Int], _ n: Int, _ m: Int, _ mx: Int) -> Bool {
        var cnt: [Int: Int] = [:]
        var l = 0, k = 0
        for r in 0..<n {
            cnt[nums[r], default: 0] += 1
            while cnt.count > mx {
                let y = nums[l]
                l += 1
                cnt[y]! -= 1
                if cnt[y] == 0 { cnt.removeValue(forKey: y) }
            }
            k += r - l + 1
            if k >= (m + 1) / 2 { return true }
        }
        return false
    }
}
