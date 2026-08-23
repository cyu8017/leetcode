// LeetCode 3823 - Reverse Letters Then Special Characters In A String
// https://leetcode.com/problems/reverse_letters_then_special_characters_in_a_string/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public String reverseByType(String s) {
        List<Character> a = new ArrayList<>();
        List<Character> b = new ArrayList<>();
        for (char c : s.toCharArray()) {
            if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z')) a.add(c);
            else b.add(c);
        }
        int j = a.size(), k = b.size();
        char[] arr = s.toCharArray();
        for (int i = 0; i < arr.length; i++) {
            if ((arr[i] >= 'A' && arr[i] <= 'Z') || (arr[i] >= 'a' && arr[i] <= 'z')) arr[i] = a.get(--j);
            else arr[i] = b.get(--k);
        }
        return new String(arr);
    }
}
