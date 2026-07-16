// LeetCode 0357 - Count Numbers with Unique Digits
// https://leetcode.com/problems/count-numbers-with-unique-digits/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function countNumbersWithUniqueDigits($n) {
        return $this->count_numbers_with_unique_digits($n);
    }

    /**
     * @param Integer $n
     * @return Integer
     */
    function count_numbers_with_unique_digits($n) {
        if ($n === 0) {
            return 1;
        }

        $total = 10;
        $unique = 9;
        $available = 9;

        for ($length = 2; $length <= $n; $length++) {
            $unique *= $available;
            $available--;
            $total += $unique;
        }

        return $total;
    }
}
