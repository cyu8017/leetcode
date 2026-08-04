// LeetCode 1268 - Search Suggestions System
// https://leetcode.com/problems/search-suggestions-system/

class Solution {
    fun suggestedProducts(products: Array<String>, searchWord: String): List<List<String>> {
        products.sort()
        val answer = mutableListOf<List<String>>()
        val prefix = StringBuilder()
        for (ch in searchWord) {
            prefix.append(ch)
            val p = prefix.toString()
            val i = lowerBound(products, p)
            val row = mutableListOf<String>()
            var j = i
            while (j < products.size && j < i + 3) {
                if (products[j].startsWith(p)) row.add(products[j]) else break
                j++
            }
            answer.add(row)
        }
        return answer
    }

    private fun lowerBound(arr: Array<String>, target: String): Int {
        var lo = 0
        var hi = arr.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (arr[mid] < target) lo = mid + 1 else hi = mid
        }
        return lo
    }
}
