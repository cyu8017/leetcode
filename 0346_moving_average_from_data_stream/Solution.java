// LeetCode 0346 - Moving Average from Data Stream

// https://leetcode.com/problems/moving-average-from-data-stream/



import java.util.ArrayDeque;

import java.util.Deque;



class MovingAverage {

    private final int size;

    private final Deque<Integer> values = new ArrayDeque<>();

    private int total;



    public MovingAverage(int size) {

        this.size = size;

    }



    public double next(int val) {

        values.offerLast(val);

        total += val;

        if (values.size() > size) {

            total -= values.pollFirst();

        }

        return (double) total / values.size();

    }

}
