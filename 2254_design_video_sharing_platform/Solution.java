// LeetCode 2254 - Design Video Sharing Platform
// https://leetcode.com/problems/design-video-sharing-platform/

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class VideoSharingPlatform {
    private int nextID = 0;
    private PriorityQueue<Integer> free = new PriorityQueue<>();
    private Map<Integer, String> videos = new HashMap<>();
    private Map<Integer, Integer> views = new HashMap<>();
    private Map<Integer, Integer> likes = new HashMap<>();
    private Map<Integer, Integer> dislikes = new HashMap<>();

    public VideoSharingPlatform() {}

    public int upload(String video) {
        int id = free.isEmpty() ? nextID++ : free.poll();
        videos.put(id, video);
        views.put(id, 0);
        likes.put(id, 0);
        dislikes.put(id, 0);
        return id;
    }

    public void remove(int videoId) {
        if (!videos.containsKey(videoId)) return;
        videos.remove(videoId);
        views.remove(videoId);
        likes.remove(videoId);
        dislikes.remove(videoId);
        free.offer(videoId);
    }

    public String watch(int videoId, int startMinute, int endMinute) {
        String v = videos.get(videoId);
        if (v == null) return "-1";
        views.put(videoId, views.get(videoId) + 1);
        if (startMinute >= v.length()) return "";
        endMinute = Math.min(endMinute, v.length() - 1);
        return v.substring(startMinute, endMinute + 1);
    }

    public void like(int videoId) {
        if (videos.containsKey(videoId)) likes.put(videoId, likes.get(videoId) + 1);
    }

    public void dislike(int videoId) {
        if (videos.containsKey(videoId)) dislikes.put(videoId, dislikes.get(videoId) + 1);
    }

    public int[] getLikesAndDislikes(int videoId) {
        if (!videos.containsKey(videoId)) return new int[] { -1 };
        return new int[] { likes.get(videoId), dislikes.get(videoId) };
    }

    public int getViews(int videoId) {
        if (!videos.containsKey(videoId)) return -1;
        return views.get(videoId);
    }
}
