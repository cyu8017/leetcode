// LeetCode 1534 - Count Good Triplets
// https://leetcode.com/problems/count-good-triplets/

import kotlin.math.abs

class Solution {
    fun countGoodTriplets(arr: IntArray, a: Int, b: Int, c: Int): Int {
        var answer = 0
        for (i in arr.indices) {
            for (j in i + 1 until arr.size) {
                if (abs(arr[i] - arr[j]) > a) continue
                for (k in j + 1 until arr.size) {
                    if (abs(arr[j] - arr[k]) <= b && abs(arr[i] - arr[k]) <= c) answer++
                }
            }
        }
        return answer
    }
}
