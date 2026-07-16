// LeetCode 0405 - Convert a Number to Hexadecimal
// https://leetcode.com/problems/convert-a-number-to-hexadecimal/

class Solution {
    /**
     * @param Integer $num
     * @return String
     */
    function toHex($num) {
        return $this->to_hex($num);
    }

    /**
     * @param Integer $num
     * @return String
     */
    function to_hex($num) {
        if ($num === 0) {
            return "0";
        }

        $digits = "0123456789abcdef";
        $value = $num & 0xFFFFFFFF;
        $result = [];

        while ($value !== 0) {
            $result[] = $digits[$value & 15];
            $value >>= 4;
        }

        return implode("", array_reverse($result));
    }
}
