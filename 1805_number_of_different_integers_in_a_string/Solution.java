// LeetCode 1805 - Number of Different Integers in a String
// https://leetcode.com/problems/number-of-different-integers-in-a-string/

import java.util.HashSet;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Solution {
    public int numDifferentIntegers(String word) {
        Set<Integer> seen = new HashSet<>();
        Matcher matcher = Pattern.compile("\\d+").matcher(word);
        while (matcher.find()) {
            seen.add(Integer.parseInt(matcher.group()));
        }
        return seen.size();
    }
}
