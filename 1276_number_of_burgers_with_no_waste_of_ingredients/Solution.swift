// LeetCode 1276 - Number of Burgers with No Waste of Ingredients
// https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

class Solution {
    func numOfBurgers(_ tomatoSlices: Int, _ cheeseSlices: Int) -> [Int] {
        if tomatoSlices % 2 != 0 { return [] }
        let jumbo = tomatoSlices / 2 - cheeseSlices
        let small = cheeseSlices - jumbo
        if jumbo < 0 || small < 0 { return [] }
        return [jumbo, small]
    }
}
