// LeetCode 0412 - Fizz Buzz
// https://leetcode.com/problems/fizz-buzz/

class Solution {
    /**
     * @param Integer $n
     * @return String[]
     */
    function fizzBuzz($n) {
        return $this->fizz_buzz($n);
    }

    /**
     * @param Integer $n
     * @return String[]
     */
    function fizz_buzz($n) {
        $result = [];
        for ($value = 1; $value <= $n; $value++) {
            if ($value % 15 === 0) {
                $result[] = "FizzBuzz";
            } elseif ($value % 3 === 0) {
                $result[] = "Fizz";
            } elseif ($value % 5 === 0) {
                $result[] = "Buzz";
            } else {
                $result[] = (string)$value;
            }
        }
        return $result;
    }
}
