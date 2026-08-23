// LeetCode 2785 - Sort Vowels in a String
// https://leetcode.com/problems/sort-vowels-in-a-string/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public String sortVowels(String s) {
        List<Character> vowels = new ArrayList<>();
        for (char c : s.toCharArray()) if (isVowel(c)) vowels.add(c);
        Collections.sort(vowels);
        char[] arr = s.toCharArray();
        int vi = 0;
        for (int i = 0; i < arr.length; i++) if (isVowel(arr[i])) arr[i] = vowels.get(vi++);
        return new String(arr);
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
            || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
    }
}
