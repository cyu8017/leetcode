// LeetCode 0352 - Data Stream as Disjoint Intervals

// https://leetcode.com/problems/data-stream-as-disjoint-intervals/



class SummaryRanges {

    private val intervals = mutableListOf<IntArray>()



    fun addNum(value: Int) {

        val newInterval = intArrayOf(value, value)

        val merged = mutableListOf<IntArray>()

        var inserted = false



        for (interval in intervals) {

            if (interval[1] < value - 1) {

                merged.add(interval)

            } else if (interval[0] > value + 1) {

                if (!inserted) {

                    merged.add(newInterval)

                    inserted = true

                }

                merged.add(interval)

            } else {

                newInterval[0] = minOf(newInterval[0], interval[0])

                newInterval[1] = maxOf(newInterval[1], interval[1])

            }

        }



        if (!inserted) {

            merged.add(newInterval)

        }



        intervals.clear()

        intervals.addAll(merged)

    }



    fun getIntervals(): List<IntArray> {

        return intervals

    }

}
