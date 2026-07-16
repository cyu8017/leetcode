// LeetCode 0049 - Group Anagrams
// https://leetcode.com/problems/group-anagrams/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> groups = new HashMap<>();

        for (String word : strs) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);
            groups.computeIfAbsent(key, k -> new ArrayList<>()).add(word);
        }

        List<List<String>> result = new ArrayList<>();
        for (List<String> group : groups.values()) {
            group.sort(String::compareTo);
            result.add(group);
        }
        result.sort((a, b) -> Integer.compare(
            minIndex(strs, b),
            minIndex(strs, a)
        ));
        return result;
    }

    private int minIndex(String[] strs, List<String> group) {
        int min = strs.length;
        for (String word : group) {
            for (int i = 0; i < strs.length; i++) {
                if (strs[i].equals(word)) {
                    min = Math.min(min, i);
                    break;
                }
            }
        }
        return min;
    }
}
