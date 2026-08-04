// LeetCode 1311 - Get Watched Videos By Your Friends
// https://leetcode.com/problems/get-watched-videos-by-your-friends/

import java.util.*;

class Solution {
    public List<String> watchedVideosByFriends(List<List<String>> watchedVideos, int[][] friends, int id, int level) {
        Queue<int[]> queue = new ArrayDeque<>();
        boolean[] seen = new boolean[friends.length];
        queue.offer(new int[]{id, 0});
        seen[id] = true;
        List<Integer> people = new ArrayList<>();
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int person = cur[0], distance = cur[1];
            if (distance == level) {
                people.add(person);
                continue;
            }
            for (int friend : friends[person]) {
                if (!seen[friend]) {
                    seen[friend] = true;
                    queue.offer(new int[]{friend, distance + 1});
                }
            }
        }
        Map<String, Integer> counts = new HashMap<>();
        for (int person : people) {
            for (String video : watchedVideos.get(person)) {
                counts.merge(video, 1, Integer::sum);
            }
        }
        List<String> answer = new ArrayList<>(counts.keySet());
        answer.sort((a, b) -> {
            int c = Integer.compare(counts.get(a), counts.get(b));
            return c != 0 ? c : a.compareTo(b);
        });
        return answer;
    }
}
