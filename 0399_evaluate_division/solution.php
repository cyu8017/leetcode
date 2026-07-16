// LeetCode 0399 - Evaluate Division
// https://leetcode.com/problems/evaluate-division/

class Solution {
    /**
     * @param String[][] $equations
     * @param Float[] $values
     * @param String[][] $queries
     * @return Float[]
     */
    function calcEquation($equations, $values, $queries) {
        return $this->calc_equation($equations, $values, $queries);
    }

    /**
     * @param String[][] $equations
     * @param Float[] $values
     * @param String[][] $queries
     * @return Float[]
     */
    function calc_equation($equations, $values, $queries) {
        $graph = [];

        foreach ($equations as $index => $equation) {
            [$dividend, $divisor] = $equation;
            $value = $values[$index];
            if (!isset($graph[$dividend])) {
                $graph[$dividend] = [];
            }
            if (!isset($graph[$divisor])) {
                $graph[$divisor] = [];
            }
            $graph[$dividend][$divisor] = $value;
            $graph[$divisor][$dividend] = 1.0 / $value;
        }

        $dfs = function ($start, $end, $visited) use (&$dfs, &$graph) {
            if (!isset($graph[$start]) || !isset($graph[$end])) {
                return -1.0;
            }
            if ($start === $end) {
                return 1.0;
            }
            $visited[$start] = true;
            foreach ($graph[$start] as $neighbor => $weight) {
                if (isset($visited[$neighbor])) {
                    continue;
                }
                $result = $dfs($neighbor, $end, $visited);
                if ($result !== -1.0) {
                    return $weight * $result;
                }
            }
            return -1.0;
        };

        $answers = [];
        foreach ($queries as $query) {
            [$start, $end] = $query;
            $answers[] = $dfs($start, $end, []);
        }

        return $answers;
    }
}
