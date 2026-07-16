// LeetCode 0282 - Expression Add Operators
// https://leetcode.com/problems/expression-add-operators/

class Solution {
    /**
     * @param String $num
     * @param Integer $target
     * @return String[]
     */
    function addOperators($num, $target) {
        $result = [];
        $length = strlen($num);

        $backtrack = function ($index, $path, $value, $previous) use (
            &$backtrack,
            $num,
            $target,
            $length,
            &$result
        ) {
            if ($index === $length) {
                if ($value === $target) {
                    $result[] = $path;
                }
                return;
            }
            for ($end = $index; $end < $length; $end++) {
                if ($end > $index && $num[$index] === "0") {
                    break;
                }
                $currentStr = substr($num, $index, $end - $index + 1);
                $current = (int)$currentStr;
                if ($index === 0) {
                    $backtrack($end + 1, $currentStr, $current, $current);
                } else {
                    $backtrack($end + 1, $path . "+" . $currentStr, $value + $current, $current);
                    $backtrack($end + 1, $path . "-" . $currentStr, $value - $current, -$current);
                    $backtrack(
                        $end + 1,
                        $path . "*" . $currentStr,
                        $value - $previous + $previous * $current,
                        $previous * $current
                    );
                }
            }
        };

        $backtrack(0, "", 0, 0);
        return $result;
    }
}
