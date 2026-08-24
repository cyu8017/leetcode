// LeetCode 2456 - Most Popular Video Creator
// https://leetcode.com/problems/most-popular-video-creator/

class Solution {
    func mostPopularCreator(_ creators: [String], _ ids: [String], _ views: [Int]) -> [[String]] {
        var total = [String: Int]()
        var bestID = [String: String]()
        var bestViews = [String: Int]()
        var maxTotal = 0
        for i in 0..<creators.count {
            let c = creators[i]
            total[c, default: 0] += views[i]
            if bestID[c] == nil {
                bestID[c] = ids[i]
                bestViews[c] = views[i]
            } else if views[i] > bestViews[c]! || (views[i] == bestViews[c]! && ids[i] < bestID[c]!) {
                bestViews[c] = views[i]
                bestID[c] = ids[i]
            }
            maxTotal = max(maxTotal, total[c]!)
        }
        var ans = [[String]]()
        for (c, t) in total where t == maxTotal {
            ans.append([c, bestID[c]!])
        }
        return ans
    }
}
