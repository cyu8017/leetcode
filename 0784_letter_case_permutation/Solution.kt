// LeetCode 0784 - Letter Case Permutation
// https://leetcode.com/problems/letter-case-permutation/

class Solution {
    fun letterCasePermutation(s: String): MutableList<String> {
        var result = ArrayList<String>()
        result.add("")
        for (ch in s.toCharArray()) {
            var next = ArrayList<String>()
            if (Character.isLetter(ch)) {
                var lower = Character.toLowerCase(ch)
                var upper = Character.toUpperCase(ch)
                for (prefix in result) {
                    next.add(prefix + lower)
                    next.add(prefix + upper)
                }
            } else {
                for (prefix in result) { next.add(prefix + ch) }
            }
            result = next
        }
        return result
    }
}
