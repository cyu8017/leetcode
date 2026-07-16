// LeetCode 0388 - Longest Absolute File Path
// https://leetcode.com/problems/longest-absolute-file-path/

class Solution {
    /**
     * @param String $input
     * @return Integer
     */
    function lengthLongestPath($input) {
        return $this->length_longest_path($input);
    }

    /**
     * @param String $input
     * @return Integer
     */
    function length_longest_path($input) {
        $stack = [];
        $maxLength = 0;
        $lines = explode("\n", $input);

        foreach ($lines as $line) {
            $depth = 0;
            $lineLength = strlen($line);
            while ($depth < $lineLength && $line[$depth] === "\t") {
                $depth++;
            }
            $name = substr($line, $depth);

            while (count($stack) > $depth) {
                array_pop($stack);
            }

            if (strpos($name, '.') !== false) {
                $prefix = count($stack) === 0 ? 0 : $stack[count($stack) - 1];
                $maxLength = max($maxLength, strlen($name) + $prefix);
            } else {
                $prefix = count($stack) === 0 ? 0 : $stack[count($stack) - 1];
                $stack[] = $prefix + strlen($name) + 1;
            }
        }

        return $maxLength;
    }
}
