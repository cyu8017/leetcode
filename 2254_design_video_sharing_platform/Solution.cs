// LeetCode 2254 - Design Video Sharing Platform
// https://leetcode.com/problems/design-video-sharing-platform/

using System;
using System.Collections.Generic;

public class VideoSharingPlatform {
    int nextID = 0;
    PriorityQueue<int, int> free = new PriorityQueue<int, int>();
    Dictionary<int, string> videos = new Dictionary<int, string>();
    Dictionary<int, int> views = new Dictionary<int, int>();
    Dictionary<int, int> likes = new Dictionary<int, int>();
    Dictionary<int, int> dislikes = new Dictionary<int, int>();

    public VideoSharingPlatform() {}

    public int Upload(string video) {
        int id;
        if (free.Count > 0) free.TryDequeue(out id, out _);
        else id = nextID++;
        videos[id] = video;
        views[id] = likes[id] = dislikes[id] = 0;
        return id;
    }

    public void Remove(int videoId) {
        if (!videos.ContainsKey(videoId)) return;
        videos.Remove(videoId);
        views.Remove(videoId);
        likes.Remove(videoId);
        dislikes.Remove(videoId);
        free.Enqueue(videoId, videoId);
    }

    public string Watch(int videoId, int startMinute, int endMinute) {
        if (!videos.TryGetValue(videoId, out string v)) return "-1";
        views[videoId]++;
        if (startMinute >= v.Length) return "";
        endMinute = Math.Min(endMinute, v.Length - 1);
        return v.Substring(startMinute, endMinute - startMinute + 1);
    }

    public void Like(int videoId) {
        if (videos.ContainsKey(videoId)) likes[videoId]++;
    }

    public void Dislike(int videoId) {
        if (videos.ContainsKey(videoId)) dislikes[videoId]++;
    }

    public int[] GetLikesAndDislikes(int videoId) {
        if (!videos.ContainsKey(videoId)) return new int[] { -1 };
        return new int[] { likes[videoId], dislikes[videoId] };
    }

    public int GetViews(int videoId) {
        if (!videos.ContainsKey(videoId)) return -1;
        return views[videoId];
    }
}
