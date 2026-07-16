// LeetCode 0372 - Super Pow
// https://leetcode.com/problems/super-pow/

class Solution {
    /**
     * @param Integer $a
     * @param Integer[] $b
     * @return Integer
     */
    function superPow($a, $b) {
        return $this->super_pow($a, $b);
    }

    /**
     * @param Integer $a
     * @param Integer[] $b
     * @return Integer
     */
    function super_pow($a, $b) {
        $mod = 1337;
        $a %= $mod;
        $result = 1;

        foreach ($b as $digit) {
            $result = $this->powMod($result, 10, $mod) * $this->powMod($a, $digit, $mod) % $mod;
        }

        return $result;
    }

    /**
     * @param Integer $base
     * @param Integer $exponent
     * @param Integer $mod
     * @return Integer
     */
    private function powMod($base, $exponent, $mod) {
        $result = 1;
        while ($exponent > 0) {
            if ($exponent & 1) {
                $result = $result * $base % $mod;
            }
            $base = $base * $base % $mod;
            $exponent >>= 1;
        }
        return $result;
    }
}
