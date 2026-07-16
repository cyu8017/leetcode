// LeetCode 0352 - Data Stream as Disjoint Intervals

// https://leetcode.com/problems/data-stream-as-disjoint-intervals/



using System.Collections.Generic;



public class SummaryRanges {

    private readonly List<int[]> intervals = new();



    public SummaryRanges() {

    }



    public void AddNum(int value) {

        int[] newInterval = new int[] {value, value};

        List<int[]> merged = new();

        bool inserted = false;



        foreach (int[] interval in intervals) {

            if (interval[1] < value - 1) {

                merged.Add(interval);

            } else if (interval[0] > value + 1) {

                if (!inserted) {

                    merged.Add(newInterval);

                    inserted = true;

                }

                merged.Add(interval);

            } else {

                newInterval[0] = Math.Min(newInterval[0], interval[0]);

                newInterval[1] = Math.Max(newInterval[1], interval[1]);

            }

        }



        if (!inserted) {

            merged.Add(newInterval);

        }



        intervals.Clear();

        intervals.AddRange(merged);

    }



    public IList<int[]> GetIntervals() {

        return intervals;

    }

}
