// LeetCode 0342 - Power of Four

// https://leetcode.com/problems/power-of-four/



class Solution {

    fun isPowerOfFour(n: Int): Boolean {

        return n > 0 && (n and (n - 1)) == 0 && n % 3 == 1

    }

}
