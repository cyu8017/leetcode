// LeetCode 3267 - Count Almost Equal Pairs II
// https://leetcode.com/problems/count-almost-equal-pairs-ii/

class Solution {
    private var sa = ""
    private var sb = ""

    func countPairs(_ nums: [Int]) -> Int {
        var ans = 0
        for i in 0..<nums.count {
            for j in (i + 1)..<nums.count where almostEqual(nums[i], nums[j]) { ans += 1 }
        }
        return ans
    }

    private func almostEqual(_ a: Int, _ b: Int) -> Bool {
        sa = String(a)
        sb = String(b)
        while sa.count < sb.count { sa = "0" + sa }
        while sb.count < sa.count { sb = "0" + sb }
        if sa == sb { return true }
        return dfs(Array(sa), 0, 2)
    }

    private func dfs(_ arr: [Character], _ start: Int, _ left: Int) -> Bool {
        var arr = arr
        if String(arr) == sb { return true }
        if left == 0 { return false }
        let target = Array(sb)
        for i in start..<arr.count {
            if arr[i] == target[i] { continue }
            if i + 1 < arr.count {
                for j in (i + 1)..<arr.count where arr[j] == target[i] {
                    arr.swapAt(i, j)
                    if dfs(arr, i + 1, left - 1) { return true }
                    arr.swapAt(i, j)
                }
            }
            return false
        }
        return String(arr) == sb
    }
}
