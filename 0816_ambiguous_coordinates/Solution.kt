// LeetCode 0816 - Ambiguous Coordinates
// https://leetcode.com/problems/ambiguous-coordinates/

class Solution {
    fun ambiguousCoordinates(s: String): MutableList<String> {
        var digits = s.substring(1, s.length - 1)
        var answer = ArrayList<String>()
        for (i in 1 until digits.length) {
            for (left in candidates(digits.substring(0, i))) {
                for (right in candidates(digits.substring(i))) {
                    answer.add("(" + left + ", " + right + ")")
                }
            }
        }
        return answer
    }

    private fun candidates(frag: String): MutableList<String> {
        var options = ArrayList<String>()
        if (frag.isEmpty() || (frag.length > 1 && frag[0] == '0' && frag[frag.length - 1] == '0')) {
            return options
        }
        if (frag[0] == '0' && frag.length > 1) {
            if (frag[frag.length - 1] != '0') options.add("0." + frag.substring(1))
            return options
        }
        options.add(frag)
        if (frag[frag.length - 1] == '0') return options
        for (i in 1 until frag.length) {
            options.add(frag.substring(0, i) + "." + frag.substring(i))
        }
        return options
    }
}
