# LeetCode 1311 - Get Watched Videos By Your Friends
# https://leetcode.com/problems/get-watched-videos-by-your-friends/

def watched_videos_by_friends(watched_videos, friends, id, level)
  queue = [[id, 0]]
  seen = { id => true }
  people = []
  until queue.empty?
    person, distance = queue.shift
    if distance == level
      people << person
      next
    end
    friends[person].each do |friend|
      next if seen[friend]
      seen[friend] = true
      queue << [friend, distance + 1]
    end
  end
  counts = Hash.new(0)
  people.each { |person| watched_videos[person].each { |video| counts[video] += 1 } }
  counts.keys.sort_by { |video| [counts[video], video] }
end
