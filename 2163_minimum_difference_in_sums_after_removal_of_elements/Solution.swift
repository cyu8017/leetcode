// LeetCode 2163 - Minimum Difference in Sums After Removal of Elements
// https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/

class Solution {
    func minimumDifference(_ nums: [Int]) -> Int {
        let n = nums.count / 3
        var left = [Int](repeating: 0, count: nums.count)
        var right = [Int](repeating: 0, count: nums.count)
        var hmax = [Int]()
        var sum = 0
        func pushMax(_ x: Int) {
            hmax.append(x)
            var i = hmax.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                if hmax[p] >= hmax[i] { break }
                hmax.swapAt(p, i); i = p
            }
        }
        func popMax() -> Int {
            let top = hmax[0]
            hmax[0] = hmax.removeLast()
            if !hmax.isEmpty {
                var i = 0
                while true {
                    var w = i
                    let l = 2 * i + 1, r = 2 * i + 2
                    if l < hmax.count && hmax[l] > hmax[w] { w = l }
                    if r < hmax.count && hmax[r] > hmax[w] { w = r }
                    if w == i { break }
                    hmax.swapAt(i, w); i = w
                }
            }
            return top
        }
        for i in 0..<n { pushMax(nums[i]); sum += nums[i] }
        left[n - 1] = sum
        for i in n..<(2 * n) {
            pushMax(nums[i]); sum += nums[i]; sum -= popMax()
            left[i] = sum
        }
        var hmin = [Int]()
        func pushMin(_ x: Int) {
            hmin.append(x)
            var i = hmin.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                if hmin[p] <= hmin[i] { break }
                hmin.swapAt(p, i); i = p
            }
        }
        func popMin() -> Int {
            let top = hmin[0]
            hmin[0] = hmin.removeLast()
            if !hmin.isEmpty {
                var i = 0
                while true {
                    var w = i
                    let l = 2 * i + 1, r = 2 * i + 2
                    if l < hmin.count && hmin[l] < hmin[w] { w = l }
                    if r < hmin.count && hmin[r] < hmin[w] { w = r }
                    if w == i { break }
                    hmin.swapAt(i, w); i = w
                }
            }
            return top
        }
        sum = 0
        for i in stride(from: nums.count - 1, through: 2 * n, by: -1) { pushMin(nums[i]); sum += nums[i] }
        right[2 * n] = sum
        for i in stride(from: 2 * n - 1, through: n, by: -1) {
            pushMin(nums[i]); sum += nums[i]; sum -= popMin()
            right[i] = sum
        }
        var ans = left[n - 1] - right[n]
        for i in n..<(2 * n) { ans = min(ans, left[i] - right[i + 1]) }
        return ans
    }
}
