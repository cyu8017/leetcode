// LeetCode 2408 - Design SQL
// https://leetcode.com/problems/design-sql/

class SQL {
    private var tables: [String: [[String]]] = [:]
    private var nextID: [String: Int] = [:]

    init(_ names: [String], _ columns: [Int]) {
        for name in names {
            tables[name] = []
            nextID[name] = 1
        }
    }

    func ins(_ name: String, _ row: [String]) -> Bool {
        guard tables[name] != nil else { return false }
        let id = nextID[name]!
        nextID[name] = id + 1
        tables[name]!.append([String(id)] + row)
        return true
    }

    func rmv(_ name: String, _ rowId: Int) {
        guard var rows = tables[name] else { return }
        if let i = rows.firstIndex(where: { Int($0[0]) == rowId }) {
            rows.remove(at: i)
            tables[name] = rows
        }
    }

    func sel(_ name: String, _ rowId: Int, _ columnId: Int) -> String {
        guard let rows = tables[name] else { return "<null>" }
        for r in rows where Int(r[0]) == rowId {
            if columnId < 1 || columnId >= r.count { return "<null>" }
            return r[columnId]
        }
        return "<null>"
    }

    func exp(_ name: String) -> [String] {
        (tables[name] ?? []).map { $0.joined(separator: ",") }
    }
}
