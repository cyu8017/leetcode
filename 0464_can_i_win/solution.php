// LeetCode 0464 - Can I Win
// https://leetcode.com/problems/can-i-win/

class Solution {
    /** @var array<int, bool> */
    private $memo = [];

    /**
     * @param int $maxChoosableInteger
     * @param int $desiredTotal
     * @return bool
     */
    function canIWin($maxChoosableInteger, $desiredTotal) {
        return $this->can_i_win($maxChoosableInteger, $desiredTotal);
    }

    /**
     * @param int $maxChoosableInteger
     * @param int $desiredTotal
     * @return bool
     */
    function can_i_win($maxChoosableInteger, $desiredTotal) {
        if ($desiredTotal <= 0) {
            return true;
        }
        $total = intdiv($maxChoosableInteger * ($maxChoosableInteger + 1), 2);
        if ($total < $desiredTotal) {
            return false;
        }

        $this->memo = [];
        return $this->canWin(0, 0, $maxChoosableInteger, $desiredTotal);
    }

    private function canWin(int $state, int $currentTotal, int $maxChoosableInteger, int $desiredTotal): bool {
        if (array_key_exists($state, $this->memo)) {
            return $this->memo[$state];
        }

        for ($pick = 1; $pick <= $maxChoosableInteger; $pick++) {
            $bit = 1 << ($pick - 1);
            if (($state & $bit) !== 0) {
                continue;
            }
            if ($currentTotal + $pick >= $desiredTotal) {
                return $this->memo[$state] = true;
            }
            if (!$this->canWin($state | $bit, $currentTotal + $pick, $maxChoosableInteger, $desiredTotal)) {
                return $this->memo[$state] = true;
            }
        }

        return $this->memo[$state] = false;
    }
}
