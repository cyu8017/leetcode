// LeetCode 1452 - People Whose List of Favorite Companies Is Not a Subset of Another List
// https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/

class Solution {
    func peopleIndexes(_ favoriteCompanies: [[String]]) -> [Int] {
        let sets = favoriteCompanies.map { Set($0) }
        return sets.indices.filter { i in
            !sets.indices.contains { j in i != j && sets[i].isSubset(of: sets[j]) }
        }
    }
}
