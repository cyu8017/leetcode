// LeetCode 0319 - Bulb Switcher
// https://leetcode.com/problems/bulb-switcher/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function bulbSwitch($n) {
        return intdiv((int) sqrt($n), 1);
    }
}
