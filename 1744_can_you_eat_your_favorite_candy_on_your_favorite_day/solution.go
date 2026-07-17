// LeetCode 1744 - Can You Eat Your Favorite Candy on Your Favorite Day?
// https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/

func canEat(candiesCount []int, queries [][]int) []bool {
    prefix := make([]int, len(candiesCount)+1)
    for i, count := range candiesCount {
        prefix[i+1] = prefix[i] + count
    }
    ans := make([]bool, 0, len(queries))
    for _, query := range queries {
        candyType, day, cap := query[0], query[1], query[2]
        minEaten := day + 1
        maxEaten := (day + 1) * cap
        ans = append(ans, maxEaten > prefix[candyType] && minEaten <= prefix[candyType+1])
    }
    return ans
}
