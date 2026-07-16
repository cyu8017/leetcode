// LeetCode 0415 - Add Strings
// https://leetcode.com/problems/add-strings/

class Solution {
    /**
     * @param String $num1
     * @param String $num2
     * @return String
     */
    function addStrings($num1, $num2) {
        return $this->add_strings($num1, $num2);
    }

    /**
     * @param String $num1
     * @param String $num2
     * @return String
     */
    function add_strings($num1, $num2) {
        $index1 = strlen($num1) - 1;
        $index2 = strlen($num2) - 1;
        $carry = 0;
        $digits = [];

        while ($index1 >= 0 || $index2 >= 0 || $carry) {
            if ($index1 >= 0) {
                $carry += (int)$num1[$index1];
                $index1--;
            }
            if ($index2 >= 0) {
                $carry += (int)$num2[$index2];
                $index2--;
            }
            $digits[] = (string)($carry % 10);
            $carry = intdiv($carry, 10);
        }

        return implode("", array_reverse($digits));
    }
}
