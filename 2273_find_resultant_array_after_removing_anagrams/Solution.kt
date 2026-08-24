// LeetCode 2273 - Find Resultant Array After Removing Anagrams
// https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

class Solution {

    private fun sig(w: String): IntArray {

            var c = IntArray(26)
            for (ch in w.toCharArray()) c[ch - 'a']++
            return c

    }


    private fun eq(a: IntArray, b: IntArray): Boolean {

            for (i in 0 until 26) { if (a[i] != b[i]) return false }
            return true

    }


    fun removeAnagrams(words: Array<String>): MutableList<String> {

            var ans = ArrayList<Int>()
            ans.add(words[0])
            var prev = sig(words[0])
            for (i in 1 until words.size) {
                var cur = sig(words[i])
                if (!eq(cur, prev)) {
                    ans.add(words[i])
                    prev = cur
                }
            }
            return ans

    }

}
