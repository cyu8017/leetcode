// LeetCode 3709 - Design Exam Scores Tracker
// https://leetcode.com/problems/design-exam-scores-tracker/

#include <algorithm>
#include <vector>

class ExamTracker {
    std::vector<int> times;
    std::vector<long long> pre;
public:
    ExamTracker() : times{0}, pre{0} {}

    void record(int time, int score) {
        times.push_back(time);
        pre.push_back(pre.back() + score);
    }

    long long totalScore(int startTime, int endTime) {
        int l = (int)(std::lower_bound(times.begin(), times.end(), startTime) - times.begin()) - 1;
        int r = (int)(std::lower_bound(times.begin(), times.end(), endTime + 1) - times.begin()) - 1;
        return pre[r] - pre[l];
    }
};
