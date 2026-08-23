// LeetCode 0346 - Moving Average from Data Stream

// https://leetcode.com/problems/moving-average-from-data-stream/



using System.Collections.Generic;



public class MovingAverage {

    private readonly int size;

    private readonly Queue<int> values = new();

    private int total;



    public MovingAverage(int size) {

        this.size = size;

    }



    public double Next(int val) {

        values.Enqueue(val);

        total += val;

        if (values.Count > size) {

            total -= values.Dequeue();

        }

        return (double)total / values.Count;

    }

}
