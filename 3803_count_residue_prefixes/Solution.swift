// LeetCode 3803 - Count Residue Prefixes
// https://leetcode.com/problems/count-residue-prefixes/

class Solution {
    func residuePrefixes(_ s: String) -> Int {
        var st = Set<Character>()
        var ans = 0
        var i = 0
        for c in s {
            st.insert(c)
            if st.count == (i + 1) % 3 { ans += 1 }
            i += 1
        }
        return ans
    }
}
