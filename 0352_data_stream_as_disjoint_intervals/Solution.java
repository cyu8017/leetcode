// LeetCode 0352 - Data Stream as Disjoint Intervals

// https://leetcode.com/problems/data-stream-as-disjoint-intervals/



import java.util.ArrayList;

import java.util.List;



class SummaryRanges {

    private final List<int[]> intervals = new ArrayList<>();



    public SummaryRanges() {

    }



    public void addNum(int value) {

        int[] newInterval = new int[] {value, value};

        List<int[]> merged = new ArrayList<>();

        boolean inserted = false;



        for (int[] interval : intervals) {

            if (interval[1] < value - 1) {

                merged.add(interval);

            } else if (interval[0] > value + 1) {

                if (!inserted) {

                    merged.add(newInterval);

                    inserted = true;

                }

                merged.add(interval);

            } else {

                newInterval[0] = Math.min(newInterval[0], interval[0]);

                newInterval[1] = Math.max(newInterval[1], interval[1]);

            }

        }



        if (!inserted) {

            merged.add(newInterval);

        }



        intervals.clear();

        intervals.addAll(merged);

    }



    public List<int[]> getIntervals() {

        return intervals;

    }

}
