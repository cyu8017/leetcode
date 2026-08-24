// LeetCode 3321 - Find X-Sum of All K-Long Subarrays II
// https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/

class Solution {
    func findXSum(_ nums: [Int], _ k: Int, _ x: Int) -> [Int] {
        let n = nums.count
        var ans = Array(repeating: 0, count: n - k + 1)
        for i in 0...(n - k) {
            var freq = [Int: Int]()
            for j in i..<(i + k) { freq[nums[j], default: 0] += 1 }
            var arr = freq.map { ($0.key, $0.value) }
            arr.sort { a, b in
                if a.1 != b.1 { return a.1 > b.1 }
                return a.0 > b.0
            }
            let lim = min(x, arr.count)
            var keep = Set<Int>()
            for t in 0..<lim { keep.insert(arr[t].0) }
            var sum = 0
            for j in i..<(i + k) where keep.contains(nums[j]) { sum += nums[j] }
            ans[i] = sum
        }
        return ans
    }
}
