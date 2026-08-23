// LeetCode 2526 - Find Consecutive Integers from a Data Stream
// https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

public class DataStream {
    private int value, k, streak;

    public DataStream(int value, int k) {
        this.value = value;
        this.k = k;
        streak = 0;
    }

    public bool Consec(int num) {
        if (num == value) streak++;
        else streak = 0;
        return streak >= k;
    }
}
