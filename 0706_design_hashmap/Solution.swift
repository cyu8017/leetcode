// LeetCode 0706 - Design HashMap
// https://leetcode.com/problems/design-hashmap/

class MyHashMap {
    private var data = [Int: Int]()
    init() {}
    func put(_ key: Int, _ value: Int) { data[key] = value }
    func get(_ key: Int) -> Int { data[key] ?? -1 }
    func remove(_ key: Int) { data[key] = nil }
}
