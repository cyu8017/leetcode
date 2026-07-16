// LeetCode 0362 - Design Hit Counter

// https://leetcode.com/problems/design-hit-counter/



import java.util.ArrayDeque;

import java.util.Deque;



class HitCounter {

    private final Deque<Integer> hits = new ArrayDeque<>();



    public HitCounter() {

    }



    public void hit(int timestamp) {

        hits.addLast(timestamp);

    }



    public int getHits(int timestamp) {

        while (!hits.isEmpty() && hits.peekFirst() <= timestamp - 300) {

            hits.pollFirst();

        }

        return hits.size();

    }

}
