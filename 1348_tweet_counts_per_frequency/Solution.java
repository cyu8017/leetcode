// LeetCode 1348 - Tweet Counts Per Frequency
// https://leetcode.com/problems/tweet-counts-per-frequency/

import java.util.*;

class TweetCounts {
    private Map<String, List<Integer>> times = new HashMap<>();

    public TweetCounts() {}

    public void recordTweet(String tweetName, int time) {
        List<Integer> list = times.computeIfAbsent(tweetName, k -> new ArrayList<>());
        int idx = Collections.binarySearch(list, time);
        if (idx < 0) idx = -idx - 1;
        list.add(idx, time);
    }

    public List<Integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime) {
        int size = switch (freq) {
            case "minute" -> 60;
            case "hour" -> 3600;
            default -> 86400;
        };
        List<Integer> list = times.getOrDefault(tweetName, List.of());
        List<Integer> answer = new ArrayList<>();
        for (int start = startTime; start <= endTime; start += size) {
            int end = Math.min(endTime, start + size - 1);
            int left = lowerBound(list, start);
            int right = upperBound(list, end);
            answer.add(right - left);
        }
        return answer;
    }

    private int lowerBound(List<Integer> a, int x) {
        int lo = 0, hi = a.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a.get(mid) < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    private int upperBound(List<Integer> a, int x) {
        int lo = 0, hi = a.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a.get(mid) <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
