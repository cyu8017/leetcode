// LeetCode 0344 - Reverse String
// https://leetcode.com/problems/reverse-string/

class Solution {
    /**
     * @param String[] $s
     * @return NULL
     */
    function reverseString(&$s) {
        $this->reverse_string($s);
    }

    /**
     * @param String[] $s
     * @return NULL
     */
    function reverse_string(&$s) {
        $left = 0;
        $right = count($s) - 1;
        while ($left < $right) {
            [$s[$left], $s[$right]] = [$s[$right], $s[$left]];
            $left++;
            $right--;
        }
    }
}
