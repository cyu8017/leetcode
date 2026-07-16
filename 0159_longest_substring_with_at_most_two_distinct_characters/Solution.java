import java.util.HashMap;
import java.util.Map;

class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        Map<Character, Integer> counts = new HashMap<>();
        int left = 0, best = 0;
        for (int right = 0; right < s.length(); right++) {
            counts.merge(s.charAt(right), 1, Integer::sum);
            while (counts.size() > 2) {
                char c = s.charAt(left++);
                if (counts.merge(c, -1, Integer::sum) == 0) counts.remove(c);
            }
            best = Math.max(best, right - left + 1);
        }
        return best;
    }
}