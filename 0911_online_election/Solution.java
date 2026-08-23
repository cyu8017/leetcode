// LeetCode 0911 - Online Election
// https://leetcode.com/problems/online-election/

import java.util.*;

class TopVotedCandidate {
    private final int[] times;
    private final int[] leaders;

    public TopVotedCandidate(int[] persons, int[] times) {
        this.times = times;
        leaders = new int[persons.length];
        Map<Integer, Integer> counts = new HashMap<>();
        int leader = -1;
        for (int i = 0; i < persons.length; i++) {
            counts.put(persons[i], counts.getOrDefault(persons[i], 0) + 1);
            if (leader == -1 || counts.get(persons[i]) >= counts.get(leader)) leader = persons[i];
            leaders[i] = leader;
        }
    }

    public int q(int t) {
        int i = Arrays.binarySearch(times, t);
        if (i < 0) i = -i - 2;
        return leaders[i];
    }
}
