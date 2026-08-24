// LeetCode 3022 - Minimize OR of Remaining Elements Using Operations
// https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/

class Solution {
    func minOrAfterOperations(_ nums: [Int], _ k: Int) -> Int {
        var ans = 0, rans = 0
        for i in stride(from: 29, through: 0, by: -1) {
            let test = ans + (1 << i)
            var cnt = 0, val = 0
            for num in nums {
                if val == 0 { val = test & num }
                else { val &= test & num }
                if val != 0 { cnt += 1 }
            }
            if cnt > k { rans += 1 << i }
            else { ans += 1 << i }
        }
        return rans
    }
}
