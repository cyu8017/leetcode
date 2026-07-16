// LeetCode 0387 - First Unique Character in a String

// https://leetcode.com/problems/first-unique-character-in-a-string/



import java.util.HashMap;

import java.util.Map;



class Solution {

    public int firstUniqChar(String s) {

        Map<Character, Integer> counts = new HashMap<>();

        for (int index = 0; index < s.length(); index++) {

            char ch = s.charAt(index);

            counts.put(ch, counts.getOrDefault(ch, 0) + 1);

        }



        for (int index = 0; index < s.length(); index++) {

            if (counts.get(s.charAt(index)) == 1) {

                return index;

            }

        }

        return -1;

    }

}
