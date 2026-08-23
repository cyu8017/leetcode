// LeetCode 2526 - Find Consecutive Integers from a Data Stream
// https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream {
    int value, k, streak;
public:
    DataStream(int value, int k) : value(value), k(k), streak(0) {}

    bool consec(int num) {
        if (num == value) streak++;
        else streak = 0;
        return streak >= k;
    }
};
