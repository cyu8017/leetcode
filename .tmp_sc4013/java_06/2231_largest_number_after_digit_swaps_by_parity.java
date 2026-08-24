// LeetCode 2231 - Largest Number After Digit Swaps by Parity
// https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int largestInteger(int num) {
        List<Integer> digits = new ArrayList<>();
        for (int x = num; x > 0; x /= 10) digits.add(0, x % 10);
        List<Integer> even = new ArrayList<>();
        List<Integer> odd = new ArrayList<>();
        for (int d : digits) {
            if (d % 2 == 0) even.add(d);
            else odd.add(d);
        }
        even.sort(Collections.reverseOrder());
        odd.sort(Collections.reverseOrder());
        int ei = 0, oi = 0, ans = 0;
        for (int d : digits) {
            if (d % 2 == 0) ans = ans * 10 + even.get(ei++);
            else ans = ans * 10 + odd.get(oi++);
        }
        return ans;
    }
}
