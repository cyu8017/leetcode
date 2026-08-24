// LeetCode 3141 - Maximum Hamming Distances
// https://leetcode.com/problems/maximum-hamming-distances/

class Solution {
    fun maxHammingDistances(nums: IntArray, m: Int): IntArray {
        var dist = IntArray(1  shl  m)
        dist.fill(-1)
        var q = ArrayList<Int>()
        for (x in nums) {
            dist[x] = 0
            q.add(x)
        }
        var k = 1
        while (!q.isEmpty()) {
            var t = ArrayList<Int>()
            for (x in q) {
                for (i in 0 until m) {
                    var y = x ^ (1  shl  i)
                    if (dist[y] == -1) {
                        dist[y] = k
                        t.add(y)
                    }
                }
            }
            q = t
            k++
        }
        for (i in 0 until nums.size) {
            var x = nums[i]
            nums[i] = m - dist[x ^ ((1  shl  m) - 1)]
        }
        return nums
    }
}
