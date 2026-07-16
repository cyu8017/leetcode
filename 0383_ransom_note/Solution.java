// LeetCode 0383 - Ransom Note

// https://leetcode.com/problems/ransom-note/



import java.util.HashMap;

import java.util.Map;



class Solution {

    public boolean canConstruct(String ransomNote, String magazine) {

        Map<Character, Integer> counts = new HashMap<>();

        for (int index = 0; index < magazine.length(); index++) {

            char ch = magazine.charAt(index);

            counts.put(ch, counts.getOrDefault(ch, 0) + 1);

        }



        for (int index = 0; index < ransomNote.length(); index++) {

            char ch = ransomNote.charAt(index);

            int remaining = counts.getOrDefault(ch, 0);

            if (remaining == 0) {

                return false;

            }

            counts.put(ch, remaining - 1);

        }

        return true;

    }

}
