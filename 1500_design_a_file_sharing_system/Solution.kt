// LeetCode 1500 - Design a File Sharing System
// https://leetcode.com/problems/design-a-file-sharing-system/

import java.util.PriorityQueue
import java.util.TreeSet

class FileSharing(m: Int) {
    private val owners = HashMap<Int, TreeSet<Int>>()
    private val chunks = HashMap<Int, HashSet<Int>>()
    private val free = PriorityQueue<Int>()
    private var nextId = 1

    fun join(ownedChunks: IntArray): Int {
        val user = if (free.isNotEmpty()) free.poll() else nextId++
        val owned = HashSet<Int>()
        for (chunk in ownedChunks) {
            owned.add(chunk)
            owners.getOrPut(chunk) { TreeSet() }.add(user)
        }
        chunks[user] = owned
        return user
    }

    fun leave(userID: Int) {
        val owned = chunks.remove(userID) ?: return
        for (chunk in owned) {
            owners[chunk]?.remove(userID)
        }
        free.offer(userID)
    }

    fun request(userID: Int, chunkID: Int): List<Int> {
        val set = owners[chunkID]
        if (set == null || set.isEmpty()) return emptyList()
        val users = set.toList()
        chunks[userID]!!.add(chunkID)
        set.add(userID)
        return users
    }
}
