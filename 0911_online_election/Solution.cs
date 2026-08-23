// LeetCode 0911 - Online Election
// https://leetcode.com/problems/online-election/

using System;
using System.Collections.Generic;

public class TopVotedCandidate {
    private readonly int[] times;
    private readonly int[] leaders;

    public TopVotedCandidate(int[] persons, int[] times) {
        this.times = times;
        leaders = new int[persons.Length];
        var counts = new Dictionary<int, int>();
        int leader = -1;
        for (int i = 0; i < persons.Length; i++) {
            if (!counts.ContainsKey(persons[i])) counts[persons[i]] = 0;
            counts[persons[i]]++;
            if (leader == -1 || counts[persons[i]] >= counts[leader]) leader = persons[i];
            leaders[i] = leader;
        }
    }

    public int Q(int t) {
        int i = Array.BinarySearch(times, t);
        if (i < 0) i = ~i - 1;
        return leaders[i];
    }
}
