// LeetCode 1452 - People Whose List Of Favorite Companies Is Not A Subset Of Another List
// https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/

import java.util.*;

class Solution {
    public List<Integer> peopleIndexes(List<List<String>> favoriteCompanies) {
        List<Set<String>> sets = new ArrayList<>();
        for (List<String> list : favoriteCompanies) sets.add(new HashSet<>(list));
        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < sets.size(); i++) {
            boolean subset = false;
            for (int j = 0; j < sets.size(); j++) {
                if (i != j && sets.get(j).containsAll(sets.get(i))) {
                    subset = true;
                    break;
                }
            }
            if (!subset) answer.add(i);
        }
        return answer;
    }
}
