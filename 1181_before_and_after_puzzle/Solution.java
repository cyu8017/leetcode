// LeetCode 1181 - Before and After Puzzle
// https://leetcode.com/problems/before-and-after-puzzle/

import java.util.*;

class Solution {
    public List<String> beforeAndAfterPuzzles(String[] phrases) {
        String[][] split = new String[phrases.length][];
        for (int i = 0; i < phrases.length; i++) split[i] = phrases[i].split(" ");
        Set<String> result = new TreeSet<>();
        for (int i = 0; i < split.length; i++) {
            for (int j = 0; j < split.length; j++) {
                if (i == j) continue;
                if (split[i][split[i].length - 1].equals(split[j][0])) {
                    StringBuilder sb = new StringBuilder();
                    for (int k = 0; k < split[i].length; k++) {
                        if (k > 0) sb.append(' ');
                        sb.append(split[i][k]);
                    }
                    for (int k = 1; k < split[j].length; k++) {
                        sb.append(' ').append(split[j][k]);
                    }
                    result.add(sb.toString());
                }
            }
        }
        return new ArrayList<>(result);
    }
}
