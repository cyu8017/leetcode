// LeetCode 1196 - How Many Apples Can You Put into the Basket
// https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

class Solution {
    fun maxNumberOfApples(weight: IntArray): Int {
        weight.sort()
        var total = 0
        for (i in weight.indices) {
            total += weight[i]
            if (total > 5000) return i
        }
        return weight.size
    }
}
