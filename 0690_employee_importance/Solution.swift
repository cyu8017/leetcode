// LeetCode 0690 - Employee Importance
// https://leetcode.com/problems/employee-importance/

class Employee {
    var id: Int
    var importance: Int
    var subordinates: [Int]
    init(_ id: Int, _ importance: Int, _ subordinates: [Int]) {
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
    }
}

class Solution {
    func getImportance(_ employees: [Employee], _ id: Int) -> Int {
        var table = [Int: Employee]()
        for emp in employees { table[emp.id] = emp }
        func dfs(_ eid: Int) -> Int {
            guard let emp = table[eid] else { return 0 }
            return emp.importance + emp.subordinates.reduce(0) { $0 + dfs($1) }
        }
        return dfs(id)
    }
}
