// LeetCode 2353 - Design a Food Rating System
// https://leetcode.com/problems/design-a-food-rating-system/

class FoodRatings {
    private var cuisineOf: [String: String] = [:]
    private var ratingOf: [String: Int] = [:]
    private var foodsOf: [String: [String]] = [:]

    init(_ foods: [String], _ cuisines: [String], _ ratings: [Int]) {
        for i in 0..<foods.count {
            cuisineOf[foods[i]] = cuisines[i]
            ratingOf[foods[i]] = ratings[i]
            foodsOf[cuisines[i], default: []].append(foods[i])
        }
    }

    func changeRating(_ food: String, _ newRating: Int) {
        ratingOf[food] = newRating
    }

    func highestRated(_ cuisine: String) -> String {
        var best = ""
        var bestR = Int.min
        for f in foodsOf[cuisine]! {
            let r = ratingOf[f]!
            if r > bestR || (r == bestR && f < best) {
                bestR = r
                best = f
            }
        }
        return best
    }
}
