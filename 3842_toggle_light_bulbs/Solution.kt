// LeetCode 3842 - Toggle Light Bulbs
// https://leetcode.com/problems/toggle-light-bulbs/

class Solution {
    fun toggleLightBulbs(bulbs: IntArray): IntArray {
        var st = IntArray(101)
        for (x in bulbs) { st[x] ^= 1 }
        var ans = ArrayList<Int>()
        for (i in 0 until 101) { if (st[i] == 1) ans.add(i) }
        var out = IntArray(ans.size)
        for (i in 0 until ans.size) { out[i] = ans[i] }
        return out
    }
}
