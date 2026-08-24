// LeetCode 2785 - Sort Vowels in a String
// https://leetcode.com/problems/sort-vowels-in-a-string/

class Solution {
    fun sortVowels(s: String): String {
        var vowels = ArrayList<Char>()
        for (c in s.toCharArray()) { if (isVowel(c)) vowels.add(c) }
        vowels.sort()
        var arr = s.toCharArray()
        var vi = 0
        for (i in 0 until arr.size) { if (isVowel(arr[i])) arr[i] = vowels[vi++] }
        return String(arr)
    }

    private fun isVowel(c: Char): Boolean {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
            || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U'
    }
}
