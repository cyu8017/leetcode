// LeetCode 0006 - Zigzag Conversion
// https://leetcode.com/problems/zigzag-conversion/

class Solution {
    /**
     * @param String $s
     * @param Integer $numRows
     * @return String
     */
    function convert($s, $numRows) {
        $n = strlen($s);
        if ($numRows === 1 || $numRows >= $n) {
            return $s;
        }

        $rows = array_fill(0, $numRows, "");
        $index = 0;
        $step = 1;

        for ($i = 0; $i < $n; $i++) {
            $rows[$index] .= $s[$i];
            if ($index === 0) {
                $step = 1;
            } elseif ($index === $numRows - 1) {
                $step = -1;
            }
            $index += $step;
        }

        return implode("", $rows);
    }
}
