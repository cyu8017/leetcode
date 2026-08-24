// LeetCode 2438 - Range Product Queries of Powers
// https://leetcode.com/problems/range-product-queries-of-powers/

import java.util.ArrayList

class Solution {
    fun productQueries(n: Int, queries: Array<IntArray>): IntArray {
            var mod: Int = 1000000007
            var powers = ArrayList()
            var bit: Int = 0
    while (bit < 31) {
    
                if (((n >> bit) & 1) != 0) powers.add(1 << bit)
    
    bit = bit + 1
    }
            var ans: IntArray = IntArray(queries.size)
            var i: Int = 0
    while (i < queries.size) {
    
                var prod: Long = 1
                var j: Int = queries[i][0]
while (j <= queries[i][1]) {

                    prod = prod * powers.get(j) % mod
                ans[i] = prod
    
    i = i + 1
    }
            return ans
    }
}
j = j + 1
}
