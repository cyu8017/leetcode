// LeetCode 1487 - Making File Names Unique
// https://leetcode.com/problems/making-file-names-unique/

class Solution {
    fun getFolderNames(names: Array<String>): Array<String> {
        val used = HashMap<String, Int>()
        val ans = Array(names.size) { "" }
        for (i in names.indices) {
            val name = names[i]
            val candidate = if (name !in used) {
                name
            } else {
                var k = used[name]!!
                while ("$name($k)" in used) k++
                used[name] = k + 1
                "$name($k)"
            }
            used[candidate] = 1
            ans[i] = candidate
        }
        return ans
    }
}
