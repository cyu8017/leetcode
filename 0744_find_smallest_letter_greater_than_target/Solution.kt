// LeetCode 0744 - Find Smallest Letter Greater Than Target
// https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution {
    fun nextGreatestLetter(letters: CharArray, target: Char): Char {
        var left = 0
        var right = letters.size
        while (left < right) {
            var mid = left + (right - left) / 2
            if (letters[mid] <= target) left = mid + 1
            else right = mid
        }
        return letters[left % letters.size]
    }
}
