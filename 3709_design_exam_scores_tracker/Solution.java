// LeetCode 3709 - Design Exam Scores Tracker
// https://leetcode.com/problems/design-exam-scores-tracker/

import java.util.ArrayList;
import java.util.List;

class ExamTracker {
    private List<Integer> times;
    private List<Long> pre;

    public ExamTracker() {
        times = new ArrayList<>();
        pre = new ArrayList<>();
        times.add(0);
        pre.add(0L);
    }

    public void record(int time, int score) {
        times.add(time);
        pre.add(pre.get(pre.size() - 1) + score);
    }

    public long totalScore(int startTime, int endTime) {
        int l = lowerBound(times, startTime) - 1;
        int r = lowerBound(times, endTime + 1) - 1;
        return pre.get(r) - pre.get(l);
    }

    private static int lowerBound(List<Integer> a, int target) {
        int lo = 0, hi = a.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a.get(mid) < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
