// LeetCode 3471 - Find the Largest Almost Missing Integer
// https://leetcode.com/problems/find-the-largest-almost-missing-integer/

class Solution {
    func largestInteger(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var cnt = [Int: Int]()
        if n >= k {
            for i in 0...(n - k) {
                var seen = Set<Int>()
                for j in i..<(i + k) { seen.insert(nums[j]) }
                for x in seen { cnt[x, default: 0] += 1 }
            }
        }
        var ans = -1
        for (x, c) in cnt where c == 1 && x > ans { ans = x }
        return ans
    }
}
