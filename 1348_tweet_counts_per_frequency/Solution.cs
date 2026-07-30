// LeetCode 1348 - Tweet Counts Per Frequency
// https://leetcode.com/problems/tweet-counts-per-frequency/

using System.Collections.Generic;
public class TweetCounts {
    Dictionary<string, List<int>> times = new Dictionary<string, List<int>>();
    public TweetCounts() {}
    public void RecordTweet(string tweetName, int time) {
        if (!times.ContainsKey(tweetName)) times[tweetName] = new List<int>();
        var list = times[tweetName];
        int idx = list.BinarySearch(time);
        if (idx < 0) idx = ~idx;
        list.Insert(idx, time);
    }
    public IList<int> GetTweetCountsPerFrequency(string freq, string tweetName, int startTime, int endTime) {
        int size = freq == "minute" ? 60 : freq == "hour" ? 3600 : 86400;
        var list = times.ContainsKey(tweetName) ? times[tweetName] : new List<int>();
        var answer = new List<int>();
        for (int start = startTime; start <= endTime; start += size) {
            int end = System.Math.Min(endTime, start + size - 1);
            int left = list.BinarySearch(start); if (left < 0) left = ~left;
            int right = list.BinarySearch(end + 1); if (right < 0) right = ~right;
            answer.Add(right - left);
        }
        return answer;
    }
}
