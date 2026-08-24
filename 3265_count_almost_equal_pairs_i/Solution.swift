// LeetCode 3265 - Count Almost Equal Pairs I
// https://leetcode.com/problems/count-almost-equal-pairs-i/

class Solution {
    func countPairs(_ nums: [Int]) -> Int {
        var ans = 0
        for i in 0..<nums.count {
            for j in (i + 1)..<nums.count where almostEqual(nums[i], nums[j]) { ans += 1 }
        }
        return ans
    }

    private func almostEqual(_ a: Int, _ b: Int) -> Bool {
        var sa = Array(String(a)), sb = Array(String(b))
        while sa.count < sb.count { sa.insert("0", at: 0) }
        while sb.count < sa.count { sb.insert("0", at: 0) }
        var diff: [Int] = []
        for i in 0..<sa.count where sa[i] != sb[i] { diff.append(i) }
        if diff.isEmpty { return true }
        if diff.count != 2 { return false }
        return sa[diff[0]] == sb[diff[1]] && sa[diff[1]] == sb[diff[0]]
    }
}
