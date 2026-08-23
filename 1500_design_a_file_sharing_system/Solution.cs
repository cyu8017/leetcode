// LeetCode 1500 - Design a File Sharing System
// https://leetcode.com/problems/design-a-file-sharing-system/

using System.Collections.Generic;

public class FileSharing {
    private readonly Dictionary<int, HashSet<int>> owners = new Dictionary<int, HashSet<int>>();
    private readonly Dictionary<int, HashSet<int>> chunks = new Dictionary<int, HashSet<int>>();
    private readonly SortedSet<int> free = new SortedSet<int>();
    private int nextId = 1;

    public FileSharing(int m) {
    }

    public int Join(IList<int> ownedChunks) {
        int user;
        if (free.Count > 0) {
            user = free.Min;
            free.Remove(user);
        } else {
            user = nextId++;
        }
        chunks[user] = new HashSet<int>(ownedChunks);
        foreach (int chunk in ownedChunks) {
            if (!owners.ContainsKey(chunk)) owners[chunk] = new HashSet<int>();
            owners[chunk].Add(user);
        }
        return user;
    }

    public void Leave(int userID) {
        if (!chunks.TryGetValue(userID, out var owned)) return;
        chunks.Remove(userID);
        foreach (int chunk in owned) {
            if (owners.TryGetValue(chunk, out var set)) set.Remove(userID);
        }
        free.Add(userID);
    }

    public IList<int> Request(int userID, int chunkID) {
        if (!owners.TryGetValue(chunkID, out var set) || set.Count == 0) {
            return new List<int>();
        }
        var users = new List<int>(set);
        users.Sort();
        chunks[userID].Add(chunkID);
        set.Add(userID);
        return users;
    }
}
