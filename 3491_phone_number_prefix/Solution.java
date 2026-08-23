// LeetCode 3491 - Phone Number Prefix
// https://leetcode.com/problems/phone-number-prefix/

import java.util.Arrays;

class Solution {
    public boolean phonePrefix(String[] numbers) {
        Arrays.sort(numbers);
        for (int i = 0; i + 1 < numbers.length; i++) {
            if (numbers[i].length() <= numbers[i + 1].length()
                    && numbers[i + 1].startsWith(numbers[i]))
                return false;
        }
        return true;
    }
}
