# LeetCode 2424 - Longest Uploaded Prefix
# https://leetcode.com/problems/longest-uploaded-prefix/

class LUPrefix
  def initialize(n)
    @uploaded = Array.new(n + 2, false)
    @prefix_len = 0
  end

  def upload(video)
    @uploaded[video] = true
    @prefix_len += 1 while @uploaded[@prefix_len + 1]
    nil
  end

  def longest
    @prefix_len
  end
end
