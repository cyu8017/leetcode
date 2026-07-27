// LeetCode 1600 - Throne Inheritance
// https://leetcode.com/problems/throne-inheritance/

class ThroneInheritance {
    private let king: String
    private var children = [String: [String]]()
    private var dead = Set<String>()

    init(_ kingName: String) {
        king = kingName
    }

    func birth(_ parentName: String, _ childName: String) {
        children[parentName, default: []].append(childName)
    }

    func death(_ name: String) {
        dead.insert(name)
    }

    func getInheritanceOrder() -> [String] {
        var order = [String]()
        func visit(_ name: String) {
            if !dead.contains(name) {
                order.append(name)
            }
            for child in children[name, default: []] {
                visit(child)
            }
        }
        visit(king)
        return order
    }
}
