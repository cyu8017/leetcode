// LeetCode 0898 - Bitwise ORs of Subarrays
// https://leetcode.com/problems/bitwise-ors-of-subarrays/

class Solution {
    func subarrayBitwiseORs(_ arr: [Int]) -> Int {
        var ans = Set<Int>()
        var cur = Set<Int>()
        for x in arr {
            var nxt: Set<Int> = [x]
            for y in cur { nxt.insert(x | y) }
            cur = nxt
            ans.formUnion(cur)
        }
        return ans.count
    }
}
