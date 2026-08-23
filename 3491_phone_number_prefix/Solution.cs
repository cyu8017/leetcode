// LeetCode 3491 - Phone Number Prefix
// https://leetcode.com/problems/phone-number-prefix/

using System;

public class Solution {
    public bool PhonePrefix(string[] numbers) {
        Array.Sort(numbers, StringComparer.Ordinal);
        for (int i = 0; i + 1 < numbers.Length; i++) {
            if (numbers[i].Length <= numbers[i + 1].Length &&
                string.CompareOrdinal(numbers[i + 1], 0, numbers[i], 0, numbers[i].Length) == 0)
                return false;
        }
        return true;
    }
}
