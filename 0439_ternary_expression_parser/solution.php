// LeetCode 0439 - Ternary Expression Parser
// https://leetcode.com/problems/ternary-expression-parser/

class Solution {
    /**
     * @param string $expression
     * @return string
     */
    function parseTernary($expression) {
        return $this->parse_ternary($expression);
    }

    /**
     * @param string $expression
     * @return string
     */
    function parse_ternary($expression) {
        if (strpos($expression, "?") === false) {
            return $expression;
        }

        $separator = 2;
        $depth = 0;
        for ($index = 2; $index < strlen($expression); $index++) {
            if ($expression[$index] === "?") {
                $depth++;
            } elseif ($expression[$index] === ":") {
                if ($depth === 0) {
                    $separator = $index;
                    break;
                }
                $depth--;
            }
        }

        if ($expression[0] === "T") {
            return $this->parse_ternary(substr($expression, 2, $separator - 2));
        }
        return $this->parse_ternary(substr($expression, $separator + 1));
    }
}
