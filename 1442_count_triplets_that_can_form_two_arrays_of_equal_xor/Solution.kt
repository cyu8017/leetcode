// LeetCode 1442 - Count Triplets That Can Form Two Arrays of Equal XOR
// https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

class Solution {
    fun countTriplets(arr: IntArray): Int {
        var answer = 0
        for (i in arr.indices) {
            var value = 0
            for (k in i until arr.size) {
                value = value xor arr[k]
                if (value == 0) answer += k - i
            }
        }
        return answer
    }
}
