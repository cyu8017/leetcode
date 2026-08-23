// LeetCode 1500 - Design a File Sharing System
// https://leetcode.com/problems/design-a-file-sharing-system/

import java.util.*;

class FileSharing {
    private final Map<Integer, Set<Integer>> owners = new HashMap<>();
    private final Map<Integer, Set<Integer>> chunks = new HashMap<>();
    private final PriorityQueue<Integer> free = new PriorityQueue<>();
    private int nextId = 1;

    public FileSharing(int m) {
    }

    public int join(int[] ownedChunks) {
        int user;
        if (!free.isEmpty()) {
            user = free.poll();
        } else {
            user = nextId++;
        }
        Set<Integer> owned = new HashSet<>();
        for (int chunk : ownedChunks) {
            owned.add(chunk);
            owners.computeIfAbsent(chunk, k -> new HashSet<>()).add(user);
        }
        chunks.put(user, owned);
        return user;
    }

    public void leave(int userID) {
        Set<Integer> owned = chunks.remove(userID);
        if (owned == null) {
            return;
        }
        for (int chunk : owned) {
            Set<Integer> set = owners.get(chunk);
            if (set != null) {
                set.remove(userID);
            }
        }
        free.offer(userID);
    }

    public List<Integer> request(int userID, int chunkID) {
        Set<Integer> set = owners.get(chunkID);
        if (set == null || set.isEmpty()) {
            return new ArrayList<>();
        }
        List<Integer> users = new ArrayList<>(set);
        Collections.sort(users);
        chunks.get(userID).add(chunkID);
        set.add(userID);
        return users;
    }
}
