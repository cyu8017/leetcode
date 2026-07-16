// LeetCode 0043 - Multiply Strings
// https://leetcode.com/problems/multiply-strings/

class Solution {
    /**
     * @param String $num1
     * @param String $num2
     * @return String
     */
    function multiply($num1, $num2) {
        if ($num1 === "0" || $num2 === "0") {
            return "0";
        }

        $positions = array_fill(0, strlen($num1) + strlen($num2), 0);

        for ($i = strlen($num1) - 1; $i >= 0; $i--) {
            for ($j = strlen($num2) - 1; $j >= 0; $j--) {
                $product = ((int)$num1[$i]) * ((int)$num2[$j]);
                $low = $i + $j + 1;
                $high = $i + $j;
                $total = $product + $positions[$low];
                $positions[$low] = $total % 10;
                $positions[$high] += intdiv($total, 10);
            }
        }

        $start = 0;
        while ($start < count($positions) && $positions[$start] === 0) {
            $start++;
        }

        if ($start === count($positions)) {
            return "0";
        }

        return implode("", array_slice($positions, $start));
    }
}
