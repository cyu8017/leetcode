# LeetCode 2456 - Most Popular Video Creator
# https://leetcode.com/problems/most-popular-video-creator/

# @param {String[]} creators
# @param {String[]} ids
# @param {Integer[]} views
# @return {String[][]}
def most_popular_creator(creators, ids, views)
  mp = {}
  max_total = 0
  creators.each_index do |i|
    info = mp[creators[i]]
    if info.nil?
      info = { "total" => views[i], "bestID" => ids[i], "bestViews" => views[i] }
      mp[creators[i]] = info
    else
      info["total"] += views[i]
      if views[i] > info["bestViews"] || (views[i] == info["bestViews"] && ids[i] < info["bestID"])
        info["bestViews"] = views[i]
        info["bestID"] = ids[i]
      end
    end
    max_total = mp[creators[i]]["total"] if mp[creators[i]]["total"] > max_total
  end
  ans = []
  mp.each { |creator, info| ans << [creator, info["bestID"]] if info["total"] == max_total }
  ans
end
