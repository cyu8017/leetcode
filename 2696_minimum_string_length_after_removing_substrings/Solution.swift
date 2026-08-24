// LeetCode 2696 - Minimum String Length After Removing Substrings
// https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

class Solution {
    func minLength(_ s: String) -> Int {
        var st: [Character] = []
        for c in s {
            if let last = st.last, (last == "A" && c == "B") || (last == "C" && c == "D") {
                st.removeLast()
            } else {
                st.append(c)
            }
        }
        return st.count
    }
}
