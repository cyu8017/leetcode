// LeetCode 1282 - Group the People Given the Group Size They Belong To
// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

import java.util.*;

class Solution {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        Map<Integer, List<Integer>> pending = new HashMap<>();
        List<List<Integer>> answer = new ArrayList<>();
        for (int person = 0; person < groupSizes.length; person++) {
            int size = groupSizes[person];
            pending.computeIfAbsent(size, key -> new ArrayList<>()).add(person);
            if (pending.get(size).size() == size) {
                answer.add(pending.get(size));
                pending.put(size, new ArrayList<>());
            }
        }
        answer.sort(Comparator.comparingInt(List::size)
            .thenComparing(list -> list.toString()));
        return answer;
    }
}
