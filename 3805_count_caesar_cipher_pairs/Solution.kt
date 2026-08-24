// LeetCode 3805 - Count Caesar Cipher Pairs
// https://leetcode.com/problems/count-caesar-cipher-pairs/

class Solution {
    fun countPairs(words: Array<String>): Long {
        var cnt = HashMap<Int, Int>()
        for (word in words) {
            var s = word.toCharArray()
            var k = 'z' - s[0]
            for (i in 1 until s.size) {
                s[i] = ('a' + (s[i] - 'a' + k).toInt().toChar() % 26)
            }
            s[0] = 'z'
            var key = String(s)
            if (!cnt.containsKey(key)) cnt[key] = 0
            cnt[key] = cnt.getOrDefault(key, 0) + 1
        }
        var ans = 0
        for (v in cnt.values) ans += v * (v - 1) / 2
        return ans
    }
}
