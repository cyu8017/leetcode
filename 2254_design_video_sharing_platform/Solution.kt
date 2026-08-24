// LeetCode 2254 - Design Video Sharing Platform
// https://leetcode.com/problems/design-video-sharing-platform/

import java.util.PriorityQueue

class VideoSharingPlatform {
    private var nextID = 0
    private val free = PriorityQueue<Int>()
    private val videos = HashMap<Int, String>()
    private val views = HashMap<Int, Int>()
    private val likes = HashMap<Int, Int>()
    private val dislikes = HashMap<Int, Int>()

    constructor() {}

    fun upload(video: String): Int {
        val id = if (free.isEmpty()) nextID++ else free.poll()
        videos[id] = video
        views[id] = 0
        likes[id] = 0
        dislikes[id] = 0
        return id
    }

    fun remove(videoId: Int) {
        if (!videos.containsKey(videoId)) return
        videos.remove(videoId)
        views.remove(videoId)
        likes.remove(videoId)
        dislikes.remove(videoId)
        free.offer(videoId)
    }

    fun watch(videoId: Int, startMinute: Int, endMinute0: Int): String {
        var endMinute = endMinute0
        val v = videos[videoId] ?: return "-1"
        views[videoId] = views[videoId]!! + 1
        if (startMinute >= v.length) return ""
        endMinute = minOf(endMinute, v.length - 1)
        return v.substring(startMinute, endMinute + 1)
    }

    fun like(videoId: Int) {
        if (videos.containsKey(videoId)) likes[videoId] = likes[videoId]!! + 1
    }

    fun dislike(videoId: Int) {
        if (videos.containsKey(videoId)) dislikes[videoId] = dislikes[videoId]!! + 1
    }

    fun getLikesAndDislikes(videoId: Int): IntArray {
        if (!videos.containsKey(videoId)) return intArrayOf(-1)
        return intArrayOf(likes[videoId]!!, dislikes[videoId]!!)
    }

    fun getViews(videoId: Int): Int {
        if (!videos.containsKey(videoId)) return -1
        return views[videoId]!!
    }
}
