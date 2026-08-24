// LeetCode 0705 - Design HashSet
// https://leetcode.com/problems/design-hashset/

class MyHashSet {
    private var data = Set<Int>()
    init() {}
    func add(_ key: Int) { data.insert(key) }
    func remove(_ key: Int) { data.remove(key) }
    func contains(_ key: Int) -> Bool { data.contains(key) }
}
