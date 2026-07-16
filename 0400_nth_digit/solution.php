// LeetCode 0400 - Nth Digit
// https://leetcode.com/problems/nth-digit/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function findNthDigit($n) {
        return $this->find_nth_digit($n);
    }

    /**
     * @param Integer $n
     * @return Integer
     */
    function find_nth_digit($n) {
        $digits = 1;
        $count = 9;
        $start = 1;

        while ($n > $digits * $count) {
            $n -= $digits * $count;
            $digits++;
            $count *= 10;
            $start *= 10;
        }

        $number = $start + intdiv($n - 1, $digits);
        $numberString = (string)$number;
        return (int)$numberString[($n - 1) % $digits];
    }
}
