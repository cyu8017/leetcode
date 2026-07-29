# LeetCode 1024 - Video Stitching
# https://leetcode.com/problems/video-stitching/

# @param {Integer[][]} clips
# @param {Integer} time
# @return {Integer}
def video_stitching(clips, time)
  furthest = Array.new(time + 1, 0)
  clips.each do |start, finish|
    furthest[start] = [furthest[start], finish].max if start <= time
  end
  ans = reach = next_reach = 0
  time.times do |i|
    next_reach = [next_reach, furthest[i]].max
    next unless i == reach
    return -1 if next_reach <= i

    ans += 1
    reach = next_reach
  end
  ans
end
