// LeetCode 2756 - Query Batching
// https://leetcode.com/problems/query-batching/

class QueryBatcher {
    private let queryMultiple: ([Int]) -> [Int]
    private let t: Int
    private var pending: [Int] = []
    private var resolvers: [(Int) -> Void] = []

    init(_ queryMultiple: @escaping ([Int]) -> [Int], _ t: Int) {
        self.queryMultiple = queryMultiple
        self.t = t
    }

    func addQuery(_ query: Int, _ resolve: @escaping (Int) -> Void) {
        pending.append(query)
        resolvers.append(resolve)
    }

    func flush() {
        guard !pending.isEmpty else { return }
        let results = queryMultiple(pending)
        for i in results.indices { resolvers[i](results[i]) }
        pending.removeAll()
        resolvers.removeAll()
    }
}
