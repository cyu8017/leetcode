// LeetCode 3709 - Design Exam Scores Tracker
// https://leetcode.com/problems/design-exam-scores-tracker/

using System.Collections.Generic;

public class ExamTracker {
    List<int> times;
    List<long> pre;

    public ExamTracker() {
        times = new List<int> { 0 };
        pre = new List<long> { 0 };
    }

    public void Record(int time, int score) {
        times.Add(time);
        pre.Add(pre[pre.Count - 1] + score);
    }

    public long TotalScore(int startTime, int endTime) {
        int l = LowerBound(times, startTime) - 1;
        int r = LowerBound(times, endTime + 1) - 1;
        return pre[r] - pre[l];
    }

    static int LowerBound(List<int> a, int target) {
        int lo = 0, hi = a.Count;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
