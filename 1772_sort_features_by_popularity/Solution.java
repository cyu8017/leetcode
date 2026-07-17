// LeetCode 1772 - Sort Features by Popularity
// https://leetcode.com/problems/sort-features-by-popularity/

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    public String[] sortFeatures(String[] features, String[] responses) {
        Set<String> featureSet = new HashSet<>(Arrays.asList(features));
        Map<String, Integer> count = new HashMap<>();
        for (String response : responses) {
            Set<String> seen = new HashSet<>();
            for (String word : response.split("\\s+")) {
                if (featureSet.contains(word)) {
                    seen.add(word);
                }
            }
            for (String word : seen) {
                count.merge(word, 1, Integer::sum);
            }
        }
        String[] result = features.clone();
        Arrays.sort(result, (a, b) -> {
            int ca = count.getOrDefault(a, 0);
            int cb = count.getOrDefault(b, 0);
            if (ca != cb) {
                return Integer.compare(cb, ca);
            }
            return a.compareTo(b);
        });
        return result;
    }
}
