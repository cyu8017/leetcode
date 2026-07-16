// LeetCode 0389 - Find the Difference
// https://leetcode.com/problems/find-the-difference/

class Solution {
    /**
     * @param String $s
     * @param String $t
     * @return String
     */
    function findTheDifference($s, $t) {
        return $this->find_the_difference($s, $t);
    }

    /**
     * @param String $s
     * @param String $t
     * @return String
     */
    function find_the_difference($s, $t) {
        $xorValue = 0;
        $combined = $s . $t;
        $length = strlen($combined);
        for ($index = 0; $index < $length; $index++) {
            $xorValue ^= ord($combined[$index]);
        }
        return chr($xorValue);
    }
}
