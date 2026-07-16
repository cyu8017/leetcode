// LeetCode 0470 - Implement Rand10() Using Rand7()
// https://leetcode.com/problems/implement-rand10-using-rand7/

function rand7() {
    if (isset($GLOBALS['__rand7_sequence__'])) {
        return array_shift($GLOBALS['__rand7_sequence__']);
    }
    throw new RuntimeException('rand7 must be provided by the test harness');
}

class Solution {
    /**
     * @return int
     */
    function rand10() {
        while (true) {
            $num = (rand7() - 1) * 7 + rand7();
            if ($num <= 40) {
                return ($num - 1) % 10 + 1;
            }
        }
    }
}
