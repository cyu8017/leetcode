// LeetCode 1166 - Design File System
// https://leetcode.com/problems/design-file-system/

class FileSystem {
    private var paths: [String: Int] = ["": -1]

    func createPath(_ path: String, _ value: Int) -> Bool {
        if paths[path] != nil { return false }
        guard let idx = path.lastIndex(of: "/") else { return false }
        let parent = String(path[..<idx])
        if paths[parent] == nil { return false }
        paths[path] = value
        return true
    }

    func get(_ path: String) -> Int {
        paths[path] ?? -1
    }
}
