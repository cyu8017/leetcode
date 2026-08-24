// LeetCode 2426 - Number of Pairs Satisfying Inequality
// https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution {
    func numberOfPairs(_ nums1: [Int], _ nums2: [Int], _ diff: Int) -> Int {
        var arr = zip(nums1, nums2).map { $0 - $1 }
        var tmp = [Int](repeating: 0, count: arr.count)
        func mergeCount(_ l: Int, _ r: Int) -> Int {
            if r - l <= 1 { return 0 }
            let m = (l + r) / 2
            var ans = mergeCount(l, m) + mergeCount(m, r)
            var j = m
            for i in l..<m {
                while j < r && arr[j] < arr[i] - diff { j += 1 }
                ans += r - j
            }
            var p = l, q = m, i2 = l
            while p < m && q < r {
                if arr[p] <= arr[q] {
                    tmp[i2] = arr[p]; p += 1
                } else {
                    tmp[i2] = arr[q]; q += 1
                }
                i2 += 1
            }
            while p < m { tmp[i2] = arr[p]; p += 1; i2 += 1 }
            while q < r { tmp[i2] = arr[q]; q += 1; i2 += 1 }
            for t in l..<r { arr[t] = tmp[t] }
            return ans
        }
        return mergeCount(0, arr.count)
    }
}
