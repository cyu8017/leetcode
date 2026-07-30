// LeetCode 1311 - Get Watched Videos By Your Friends
// https://leetcode.com/problems/get-watched-videos-by-your-friends/

using System.Collections.Generic;

public class Solution {
    public IList<string> WatchedVideosByFriends(IList<IList<string>> watchedVideos, int[][] friends, int id, int level) {
        var queue = new Queue<(int, int)>();
        var seen = new HashSet<int> { id };
        queue.Enqueue((id, 0));
        var people = new List<int>();
        while (queue.Count > 0) {
            var (person, distance) = queue.Dequeue();
            if (distance == level) { people.Add(person); continue; }
            foreach (int friend in friends[person]) {
                if (seen.Add(friend)) queue.Enqueue((friend, distance + 1));
            }
        }
        var counts = new Dictionary<string, int>();
        foreach (int person in people)
            foreach (string video in watchedVideos[person]) {
                if (!counts.ContainsKey(video)) counts[video] = 0;
                counts[video]++;
            }
        var answer = new List<string>(counts.Keys);
        answer.Sort((a, b) => {
            int cmp = counts[a].CompareTo(counts[b]);
            return cmp != 0 ? cmp : string.CompareOrdinal(a, b);
        });
        return answer;
    }
}
