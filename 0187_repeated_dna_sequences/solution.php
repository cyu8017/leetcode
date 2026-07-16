// LeetCode 0187 - Repeated DNA Sequences
// https://leetcode.com/problems/repeated-dna-sequences/

class Solution {
    /**
     * @param String $s
     * @return String[]
     */
    function findRepeatedDnaSequences($s) {
        $seen = [];
        $repeated = [];

        for ($index = 0; $index <= strlen($s) - 10; $index++) {
            $sequence = substr($s, $index, 10);
            if (isset($seen[$sequence])) {
                $repeated[$sequence] = true;
            } else {
                $seen[$sequence] = true;
            }
        }

        return array_keys($repeated);
    }
}