// LeetCode 0246 - Strobogrammatic Number
// https://leetcode.com/problems/strobogrammatic-number/

using System.Collections.Generic;

public class Solution {
    public bool IsStrobogrammatic(string num) {
        Dictionary<char, char> mapping = new Dictionary<char, char> {
            ['0'] = '0',
            ['1'] = '1',
            ['6'] = '9',
            ['8'] = '8',
            ['9'] = '6',
        };

        int left = 0;
        int right = num.Length - 1;
        while (left <= right) {
            if (!mapping.TryGetValue(num[left], out char match) || match != num[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
