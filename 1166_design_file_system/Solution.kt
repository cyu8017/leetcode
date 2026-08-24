// LeetCode 1166 - Design File System
// https://leetcode.com/problems/design-file-system/

class FileSystem {
    private val paths = mutableMapOf("" to -1)

    fun createPath(path: String, value: Int): Boolean {
        if (path in paths) return false
        val idx = path.lastIndexOf('/')
        val parent = path.substring(0, idx)
        if (parent !in paths) return false
        paths[path] = value
        return true
    }

    fun get(path: String): Int = paths.getOrDefault(path, -1)
}
